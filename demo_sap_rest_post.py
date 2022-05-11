# Demo to connect to SAP REST Endpoint - Python WebClient Client 
# Create a new SAP Airport Entity SAP 
# Magdeburger Developement Days 2022 - https://md-devdays.de
# Joerg Mueller - @MDJoerg

import sap_context
import requests
import json

# ask user for new airport
airport_id = input("Enter the airport ID: ")
if airport_id == "":
    quit()

airport_name = input("Enter the airport name: ")
if airport_name == "":
    quit()

airport_timezone = input("Enter the airport timezone: ")
        

# build service url
rest_url = "http://" + sap_context.sap_host + ":" + sap_context.sap_http_port
rest_url += sap_context.sap_rest_endpoint + "/" + sap_context.sap_rest_airport
rest_url += "/" + airport_id + sap_context.sap_rest_params
print("REST URL: ", rest_url)

# build json
rest_data = {
    "NAME" : airport_name,
    "TIME_ZONE" : airport_timezone
}
rest_payload = json.dumps(rest_data)
print("REST Payload:", rest_payload)

# call sap odata service api
response = requests.post(rest_url, rest_payload)

if response.status_code != 200:
    print(f"Error {response.status_code}: {response.text}")
else:
    if response.text.find("{") != 0 and response.text.find("[") != 0:
        print("Response:", response.text)
        print("Response is not a JSON answer?!")
    else:    
        json_response = json.loads(response.text)
        print("REST Response:", json_response)