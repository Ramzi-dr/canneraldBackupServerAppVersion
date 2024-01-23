"""
class VirtualMessage:
    bs4_door_reader = "571.787.423"
    ramzi_badge = {
        "jsonrpc": "2.0",
        "method": "notify",
        "params": [
            "ObservedStates",
            {
                "data": {
                    "deviceid": bs4_door_reader,
                    "events": [
                        {
                            "condition": "Immediate",
                            "event": "RFID Media",
                            "publicMediaLabel": "000.343.682.3",
                            "systemApproved": False,
                        }
                    ],
                    "noEventsLost": True,
                    "time": "2023-07-27T10:47:39Z",
                    "type": "deviceEvent",
                },
                "event": "notification",
            },
        ],
    }
    risingEdge = {
        "jsonrpc": "2.0",
        "method": "notify",
        "params": [
            "ObservedStates",
            {
                "data": {
                    "deviceid": "565.135.012",
                    "events": [{"condition": "Rising Edge", "event": "Input 3"}],
                    "noEventsLost": True,
                    "time": "2023-08-03T11:43:23Z",
                    "type": "deviceEvent",
                },
                "event": "notification",
            },
        ],
    }
    ramzi_code = {
        "jsonrpc": "2.0",
        "method": "notify",
        "params": [
            "ObservedStates",
            {
                "data": {
                    "deviceid": bs4_door_reader,
                    "events": [{"code": "1234", "event": "Code"}],
                    "noEventsLost": True,
                    "time": "2023-07-27T10:50:29Z",
                    "type": "deviceEvent",
                },
                "event": "notification",
            },
        ],
    }

    bs1_user_code = {
        "jsonrpc": "2.0",
        "method": "notify",
        "params": [
            "ObservedStates",
            {
                "data": {
                    "deviceid": "570.823.911",
                    "events": [{"code": "1111", "event": "Code"}],
                    "noEventsLost": True,
                    "time": "2023-07-27T10:52:21Z",
                    "type": "deviceEvent",
                },
                "event": "notification",
            },
        ],
    }

    bs1_user_badge = {
        "jsonrpc": "2.0",
        "method": "notify",
        "params": [
            "ObservedStates",
            {
                "data": {
                    "deviceid": "570.823.911",
                    "events": [
                        {
                            "condition": "Immediate",
                            "event": "RFID Media",
                            "publicMediaLabel": "000.343.559.9",
                            "systemApproved": False,
                        }
                    ],
                    "noEventsLost": True,
                    "time": "2023-07-27T10:47:39Z",
                    "type": "deviceEvent",
                },
                "event": "notification",
            },
        ],
    }
    bs4UserCode = [
        "ObservedStates",
        {
            "data": {
                "deviceid": "571.787.423",
                "events": [{"code": "2222", "event": "Code"}],
                "noEventsLost": True,
                "time": "2023-07-27T10:50:29Z",
                "type": "deviceEvent",
            },
            "event": "notification",
        },
    ]

    masterBadge = [
        "ObservedStates",
        {
            "data": {
                "deviceid": "571.787.423",
                "events": [
                    {
                        "condition": "Immediate",
                        "event": "RFID Media",
                        "publicMediaLabel": "000.343.682.3",
                        "systemApproved": False,
                    }
                ],
                "noEventsLost": True,
                "time": "2023-07-27T10:48:12Z",
                "type": "deviceEvent",
            },
            "event": "notification",
        },
    ]
    masterBadgeLong = [
        "ObservedStates",
        {
            "data": {
                "deviceid": "571.787.423",
                "events": [
                    {
                        "condition": "Duration Long",
                        "event": "RFID Media",
                        "publicMediaLabel": "000.343.682.3",
                        "systemApproved": False,
                    }
                ],
                "noEventsLost": True,
                "time": "2023-07-27T10:49:48Z",
                "type": "deviceEvent",
            },
            "event": "notification",
        },
    ]

    accessPointModification = [
        "AccessPointPropertyData",
        {
            "data": {
                "modified": [
                    {"baseId": "135", "id": "542", "propertyId": "5022", "value": False}
                ]
            },
            "event": "changed",
        },
    ]
    addedOrDeletedDoor = [
        "AuthorizationPoints",
        {
            "data": {
                "added": [
                    {
                        "accessPointId": "137",
                        "actions": None,
                        "authRoles": None,
                        "class": 2,
                        "deviceId": "0",
                        "id": "284",
                        "label": "Default",
                        "options": None,
                        "outputs": None,
                        "subsystemId": "0",
                        "zones": None,
                    }
                ]
            },
            "event": "changed",
        },
    ]
    addedOrDeletedUser = [
        "UsersGroups",
        {
            "data": {
                "added": [{"class": 1, "id": "195", "label": "ali", "subsystemId": "0"}]
            },
            "event": "changed",
        },
    ]

    risingEdge = {
        "jsonrpc": "2.0",
        "method": "notify",
        "params": [
            "ObservedStates",
            {
                "data": {
                    "deviceid": "565.135.012",
                    "events": [{"condition": "Rising Edge", "event": "Input 3"}],
                    "noEventsLost": True,
                    "time": "2023-08-03T11:43:23Z",
                    "type": "deviceEvent",
                },
                "event": "notification",
            },
        ],
    }
    stateInput_1 = {
        "jsonrpc": "2.0",
        "method": "notify",
        "params": [
            "ObservedStates",
            {
                "data": {
                    "modified": [
                        {
                            "deviceid": "560.456.939",
                            "state": 1,
                            "timestamp": "2023-08-03T11:43:23.000Z",
                            "timestampChanged": "2023-08-03T11:43:23.000Z",
                            "type": 16,
                        }
                    ]
                },
                "event": "changed",
            },
        ],
    }

    fallingEdge = {
        "jsonrpc": "2.0",
        "method": "notify",
        "params": [
            "ObservedStates",
            {
                "data": {
                    "deviceid": "565.135.012",
                    "events": [{"condition": "Falling Edge", "event": "Input 3"}],
                    "noEventsLost": True,
                    "time": "2023-08-03T11:43:23Z",
                    "type": "deviceEvent",
                },
                "event": "notification",
            },
        ],
    }
    stateInput_0 = {
        "jsonrpc": "2.0",
        "method": "notify",
        "params": [
            "ObservedStates",
            {
                "data": {
                    "modified": [
                        {
                            "deviceid": "565.135.012",
                            "state": 0,
                            "timestamp": "2023-08-03T11:43:23.000Z",
                            "timestampChanged": "2023-08-03T11:43:23.000Z",
                            "type": 16,
                        }
                    ]
                },
                "event": "changed",
            },
        ],
    }
"""
