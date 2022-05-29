
# define sap context
sap_host = "10.17.1.12"
sap_http_port = "80"
sap_https_port = "443"
sap_client = "100"
sap_user = "USER"
sap_pass = "PASS"

# define OData context (alias required in sap transaction SICF)
sap_odata_params   = "?sap-client=100&$format=json"
sap_odata_endpoint = "/demos/mdd22/odata_srv"
sap_odata_flight_schedule_world = "ZC_MDD_VDMF_FS_WLD"

# define web socket context (alias required in sap transaction SICF)
sap_wsock_protocol = "ws://"
sap_wsock_path = "/demos/mdd22/apc"

# define REST context (alias required in sap transaction SICF)
sap_rest_params   = "?sap-client=100"
sap_rest_endpoint = "/demos/mdd22/rest"
sap_rest_flight_schedule_world = "FlightSchedule"
sap_rest_airport = "Airport"
