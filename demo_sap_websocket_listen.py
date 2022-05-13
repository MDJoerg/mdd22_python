# Demo to connect to SAP ABAP Push Channel as Python WebSocket Client 
# and listen to external commands
# Magdeburger Developement Days 2022 - https://md-devdays.de
# Joerg Mueller - @MDJoerg

import asyncio
import websockets
import sap_context

async def ws_listen(url, clientId):   
    async with websockets.connect(url) as websocket:
        
        print("Connect to SAP APC Websocket:", url)
        connect_msg = "connect:" + clientId + ":from python"
        print(">", connect_msg)
        await websocket.send(connect_msg)
        quit_arrived = False
        while quit_arrived == False:
            response = await websocket.recv()
            print("<", response)

            command = response
            payload = ""
            pos_sep = response.find(":")

            if  pos_sep > 0:
                command = response[:pos_sep]
                payload = response[pos_sep + 1:]
                print(f"< COMMAND detected: {command} payload = '{payload}'")

            if command == "quit":
                quit_arrived = True

# get client id
client_id = input("Enter a client ID: ")
if client_id == "":
    client_id = "test1234"

# prepare websocket url for SAP ABAP Backend
ws_url = sap_context.sap_wsock_protocol + sap_context.sap_host + ":" + sap_context.sap_http_port
ws_url += sap_context.sap_wsock_path + "?sap-client=" + sap_context.sap_client

# open listener until quit command or kill detected
try:
    asyncio.get_event_loop().run_until_complete(ws_listen(ws_url, client_id))
except KeyboardInterrupt:
    print("Cancelled by user!")

