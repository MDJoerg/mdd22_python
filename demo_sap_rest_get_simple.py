# Demo to connect to SAP OData Endpoint Python WebSocket Client 
# Get a Entity Set List and parse JSON Request
# Magdeburger Developement Days 2022 - https://md-devdays.de
# Joerg Mueller - @MDJoerg

import sap_context
import requests
import json

# optional user inpput
rest_id = input("Optional: Enter a ID: ")

# build service url
rest_url = "http://" + sap_context.sap_host + ":" + sap_context.sap_http_port
rest_url += sap_context.sap_rest_endpoint + "/" + sap_context.sap_rest_flight_schedule_world 
if rest_id != "":
    rest_url += "/" + rest_id
rest_url += sap_context.sap_rest_params
print("REST URL: ", rest_url)


# call sap odata service api
response = requests.get(rest_url)

if response.status_code != 200:
    print(f"Error {response.status_code}: {response.text}")
else:
    if response.text.find("{") != 0 and response.text.find("[") != 0:
        print("Response:", response.text)
        print("Response is not a JSON answer?!")
    else:    
        json_response = json.loads(response.text)
        print(json_response)

