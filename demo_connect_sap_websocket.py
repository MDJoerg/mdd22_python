# Demo to connect to SAP ABAP Push Channel as Python WebSocket Client 
# Magdeburger Developement Days 2022 - https://md-devdays.de
# Joerg Mueller - @MDJoerg

import asyncio
import websockets

ws_protocol = "ws://"
ws_host = "10.17.1.12"
ws_path = "/sap/bc/apc/sap/zmdd_wsps_apc"
ws_params = "?sap-client=100"

async def test():   
    ws_url = ws_protocol + ws_host + ws_path + ws_params
    print("Connect to SAP APC Websocket ", ws_url)
    async with websockets.connect(ws_url) as websocket:
        
        await websocket.send("hello! I am from python")
        quit_arrived = False
        while quit_arrived == False:
            response = await websocket.recv()
            print(response)
            if response.find("mqba-topic:quit") > 0:
                quit_arrived = True

#asyncio.get_event_loop().run_until_complete(test())