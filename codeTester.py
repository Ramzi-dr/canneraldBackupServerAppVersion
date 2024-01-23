# class WebSocketServer:
#     _instance = None

#     def __init__(self):
#         self.connected_clients = {}
#         self.reconnect_attempts_client = {}
#         self.client_ip = None
#         self.last_disconnected = 0
#         self.max_reconnect_attempts = (
#             10  # Set the maximum number of reconnection attempts
#         )

#     async def authenticate(self, websocket, path):
#         authentication_successful = False
#         client_auth = [{"ramzi": "dridi"}, {"Ramzi": "Drido"}]
#         given_auth = {}
#         reconnected_client_id = str(uuid.uuid4())  # Generate a unique ID for the client

#         await asyncio.sleep(2)
#         self.reconnect_attempts_client[reconnected_client_id] = 0

#         while not authentication_successful:
#             try:
#                 # ... (your existing code)

#                 if given_auth in client_auth:
#                     authentication_successful = True
#                     await websocket.send(json.dumps({"status": "success"}))
#                     print(f"Client {username} authenticated successfully.")
#                     del self.reconnect_attempts_client[reconnected_client_id]
#                 else:
#                     # ... (your existing code)

#                     # Check if the maximum reconnection attempts are reached
#                     if (
#                         self.reconnect_attempts_client[reconnected_client_id]
#                         >= self.max_reconnect_attempts
#                     ):
#                         print(
#                             f"Maximum reconnection attempts reached for client {username}. Closing connection."
#                         )
#                         await websocket.close()
#                         del self.reconnect_attempts_client[reconnected_client_id]
#                         break

#                     self.reconnect_attempts_client[reconnected_client_id] += 1

#             except websockets.ConnectionClosed:
#                 print("Connection closed during authentication.")
#                 break

#         return authentication_successful
