import websockets
import uuid
import json
from urllib.parse import urlparse, parse_qs
from doorsProject.emailManager import *
from doorsProject.glutzMain import run_GlutzListener, take_overToggle
from doorsProject.payloadCollection import PayloadCollection

import time

# from doorsProject.glutzMain import *


class ClientInstance:
    _instances = {}


class WebSocketServer:
    _instance = None

    def __init__(self):
        self.connected_clients = {}
        self.reconnect_attempts_client = {}
        self.client_ip = None
        self.last_disconnected = 0

    async def authenticate(self, websocket, path):
        print("im c")
        authentication_successful = False
        client_auth = [{"ramzi": "dridi"}, {"Ramzi": "Drido"}]
        given_auth = {}
        reconnected_client_id = str(uuid.uuid4())  # Generate a unique ID for the client

        await asyncio.sleep(2)
        if not authentication_successful:
            try:
                query_params = parse_qs(urlparse(path).query)
                if query_params["username"][0] and query_params["password"][0]:
                    username = query_params["username"][0]
                    password = query_params["password"][0]

                    self.reconnect_attempts_client[username] = 0
                    given_auth[username] = password
                    print(given_auth in client_auth)
                    if given_auth in client_auth:
                        authentication_successful = True
                        await websocket.send(json.dumps({"status": "success"}))
                        print(f"Client {username} authenticated successfully.")
                        del self.reconnect_attempts_client[reconnected_client_id]
                    else:
                        await websocket.send(
                            json.dumps(
                                {"status": "failure", "reason": "Invalid credentials"}
                            )
                        )
                        print(
                            f"Authentication failed for client {username}. Closing connection."
                        )
                        await websocket.close()
                        self.reconnect_attempts_client[reconnected_client_id] += 1

            except websockets.ConnectionClosed:
                print("Connection closed during authentication.")
            return authentication_successful

    async def handle_client(
        self,
        websocket,
        path,
    ):
        client_id = str(uuid.uuid4())  # Generate a unique ID for the client
        self.connected_clients[client_id] = websocket
        self.client_ip = websocket.remote_address[0]
        authentication_successful = await self.authenticate(websocket, path)
        if authentication_successful:
            ClientInstance()._instances[self.client_ip] = self
            print("Client is back")
            take_overToggle(value=False)
            await send_email(subject="The main eventServer is online", message="")
            await log_generator(
                log_message='"The main event server is online ',
                log_level_number=1,
            )
            try:
                while True:
                    message_str = await websocket.recv()
                    message = json.loads(message_str)
                    print(message)

            except websockets.ConnectionClosed as e:
                if e.code == 1000:  # 1000 denotes a normal closure
                    await log_generator(
                        log_message="Connection closed gracefully by the event server",
                        log_level_number=2,
                    )
                else:
                    await log_generator(
                        log_message=f"Connection closed unexpectedly by client {self.client_ip} with code {e.code}: {e.reason}",
                        log_level_number=3,
                    )
                print("client is out")
                await send_email(subject="The main eventServer is offline", message="")
                del self.connected_clients[client_id]
                del ClientInstance()._instances[self.client_ip]
                self.last_disconnected = time.time()

            except Exception as ex:
                await send_email(
                    subject="There is Exception in main() at the handle_client in backup server",
                    message="",
                )
                print(f"An error occurred: {ex}")
                await log_generator(
                    log_message='"An error occurred in the main() .', log_level_number=2
                )
                del ClientInstance()._instances[self.client_ip]
                self.last_disconnected = time.time()

            finally:
                await websocket.close()

    async def handle_reconnection(self):
        glutzListener_isCalled = False
        while True:
            if not ClientInstance()._instances:
                await asyncio.sleep(1)
                current_time = time.time()
                if (
                    current_time - self.last_disconnected >= 1
                    and not ClientInstance()._instances
                ):
                    print("we take over ")
                    take_overToggle(value=True)
                    if not glutzListener_isCalled:
                        await run_GlutzListener()
                        glutzListener_isCalled = True
            if ClientInstance()._instances:
                take_overToggle(value=False)
                glutzListener_isCalled = False
                await asyncio.sleep(30)

    async def start_server(self):
        server = await websockets.serve(
            self.handle_client,
            "localhost",
            PayloadCollection.backupServerPort,
            ping_timeout=None,
        )
        print("Server running...")
        await log_generator(
            log_message="The backup server is up and running!......", log_level_number=0
        )
        await asyncio.sleep(5)
        if not self.connected_clients:
            print("no client")
            await send_email(subject="The eventServer is not Connected!", message="")
        else:
            pass
        await server.wait_closed()


async def main():
    try:
        server = WebSocketServer()
        await asyncio.gather(
            server.start_server(), WebSocketServer().handle_reconnection()
        )
    except KeyboardInterrupt:
        print("Server shutting down...")
    except Exception as e:
        import traceback

        traceback.print_exc()
        print(f"An error occurred: {e}")
        await log_generator(
            log_message=f"An error occurred in main() traceback: {e}",
            log_level_number=2,
        )


if __name__ == "__main__":
        
    message = (
        """
            <p>I am pleased to inform you that Cannerald backup eventServer is now back online and fully operational, and is running smoothly.</p>
            <p>This communication serves purely as an informational notice, and no further action is required on your part.</p>"""
    )
    asyncio.run(send_email(subject='test',message=message, betrifft="backup"))
    #asyncio.run(main())

    # async def virtual_messages(self):
    #     await self.broadcast(message=VirtualMessage.bs1_user_badge)
    #     await asyncio.sleep(2)
    #     await self.broadcast(message=VirtualMessage.fallingEdge)
    #     await asyncio.sleep(2)
    #     await self.broadcast(message=VirtualMessage.bs1_user_code)
    #     await asyncio.sleep(2)
    #     await self.broadcast(message=VirtualMessage.ramzi_badge)
    #     await asyncio.sleep(1)
    #     await self.broadcast(message=VirtualMessage.risingEdge)
    #     await asyncio.sleep(1)
    #     await self.broadcast(message=VirtualMessage.ramzi_code)
    #     await asyncio.sleep(2)
    #     await self.broadcast(message=VirtualMessage.fallingEdge)
    #     await self.broadcast(message=VirtualMessage.bs1_user_badge)
    #     await self.broadcast(message=VirtualMessage.ramzi_badge)
    #     await self.broadcast(message=VirtualMessage.bs1_user_code)
    #     await self.broadcast(message=VirtualMessage.ramzi_code)
    #     await asyncio.sleep(20)
    #     await self.broadcast(message=VirtualMessage.risingEdge)

    # async def broadcast(self, message):
    #     for client_id, websocket in self.connected_clients.items():
    #         try:
    #             await websocket.send(json.dumps(message))
    #             await asyncio.sleep(2)
    #             print("message sent ")
    #         except websockets.ConnectionClosed as b:
    #             print(f"close from brad caaaa {b}")
    #             del self.connected_clients[client_id]
