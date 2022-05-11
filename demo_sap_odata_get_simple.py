# Demo to connect to SAP OData Endpoint - Python WebService Client 
# Get a Entity Set List and parse JSON Request
# Magdeburger Developement Days 2022 - https://md-devdays.de
# Joerg Mueller - @MDJoerg

import sap_context
import requests
import json

# build service url
odata_url = "http://" + sap_context.sap_host + ":" + sap_context.sap_http_port
odata_url += sap_context.sap_odata_endpoint + "/" + sap_context.sap_odata_flight_schedule_world + sap_context.sap_odata_params
print("OData URL: ", odata_url)

# call sap odata service api
response = requests.get(odata_url)

if response.status_code != 200:
    print(f"Error {response.status_code}: {response.text}")
else:
    if response.text.find("{") != 0:
        print("Response:", response.text)
        print("Response is not a JSON answer?!")
    else:    
        json_response = json.loads(response.text)
        #print(json_response)
        print("JSON output detected")
        json_results = json_response["d"]["results"]
        print("============================")
        index = 0
        for json_result in json_results:
            index += 1
            print("\nResult Index: ", index)
            for json_attribute in json_result:
                print(json_attribute, " = ", json_result[json_attribute])


