# Demo to connect to SAP REST Endpoint - Python WebClient Client 
# Delete an existing SAP Airport Record (first Char is x..Z) 
# Magdeburger Developement Days 2022 - https://md-devdays.de
# Joerg Mueller - @MDJoerg

import sap_context
import requests
import json

# ask user for new airport
airport_id = input("Enter the airport ID to delete: ")
if airport_id == "":
    quit()
        
# build service url
rest_url = "http://" + sap_context.sap_host + ":" + sap_context.sap_http_port
rest_url += sap_context.sap_rest_endpoint + "/" + sap_context.sap_rest_airport
rest_url += "/" + airport_id + sap_context.sap_rest_params
print("REST URL: ", rest_url)

# call sap odata service api
response = requests.delete(rest_url)

if response.status_code != 200:
    print(f"Error {response.status_code}: {response.text}")
else:
    if response.text.find("{") != 0 and response.text.find("[") != 0:
        print("Response:", response.text)
        print("Response is not a JSON answer?!")
    else:    
        json_response = json.loads(response.text)
        print("REST Response:", json_response)