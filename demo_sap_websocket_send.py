# Demo to connect to SAP ABAP Push Channel as Python WebSocket Client 
# and send a command
# Magdeburger Developement Days 2022 - https://md-devdays.de
# Joerg Mueller - @MDJoerg

import asyncio
import websockets
import sap_context

async def sap_websocket_send(url, message):   
    async with websockets.connect(url) as websocket:
        
        print("Connect to SAP APC Websocket:", url)
        print(">", message)
        await websocket.send(message)
        response = await websocket.recv()
        print("<", response)

# enter message
msg = input("Enter the message: ")
if msg != "":
    # prepare websocket url for SAP ABAP Backend
    ws_url = sap_context.sap_wsock_protocol + sap_context.sap_host + ":" + sap_context.sap_http_port
    ws_url += sap_context.sap_wsock_path + "?sap-client=" + sap_context.sap_client

    # open listener until quit command or kill detected
    asyncio.get_event_loop().run_until_complete(sap_websocket_send(ws_url, msg))
