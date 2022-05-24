# note: we switched to a reserved sandbox, so login here looks differentimport requests
import json
import sys
import requests

# Authentication to sd-wan uses request sessions: endpoint, username, and password must be specified with special 'j_*' format
base_url = "https://10.10.20.90/"
auth_endpoint = "j_security_check"

login_body = {
    "j_username": "admin",
    "j_password": "C1sco12345"
}

# Session maintains key and serves as our way of interacting with sd-wan api once successfully authenticated
sesh = requests.session()

# Note: json convesition not necessary here for 'data'
login_response = sesh.post(url=f"{base_url}{auth_endpoint}", data=login_body, verify=False)

# login response.ok means 200 response, text body will be empty unless a failure occurs
if not login_response.ok or login_response.text:
    print('login failed')
    sys.exit(1)
else:
    print('login succeeded')

# Need cross site scripting token for post requests
cross_endpoint = "dataservice/client/token"
cross_response = sesh.get(url=f"{base_url}{cross_endpoint}", verify=False)
sesh.headers["X-XSRF-TOKEN"] = cross_response.content


# retrieve all devices that have certs supplied
cert_endpoint = "dataservice/certificate/vsmart/list"

headers = {
    "Accept": "application/json",
}

# response = sesh.get(url = f"{base_url}{cert_endpoint}", headers=headers, verify=False).json()
# print(json.dumps(response, indent=2))


# retrieve the root certificate
root_endpoint = "dataservice/certificate/rootcertificate"

response = sesh.get(url = f"{base_url}{root_endpoint}", headers=headers, verify=False).json()

print(json.dumps(response, indent=2))