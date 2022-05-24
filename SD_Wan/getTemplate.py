import requests
import json
import sys

# Authentication to sd-wan uses request sessions: endpoint, username, and password must be specified with special 'j_*' format
base_url = "https://10.10.20.90/"
auth_endpoint = "j_security_check"

login_body = {
    "j_username": "admin",
    "j_password": "C1sco12345"
}

header = {
    "Content-Type": "application/x-www-form-urlencoded"
}

# Session maintains key and serves as our way of interacting with sd-wan api once successfully authenticated
sesh = requests.session()

# Note: json convesition not necessary here for 'data'
login_response = sesh.post(url=f"{base_url}{auth_endpoint}", data=login_body, headers=header, verify=False)

# login response.ok means 200 response, text body will be empty unless a failure occurs
if not login_response.ok or login_response.text:
    print('login failed')
    sys.exit(1)
else:
    print('login succeeded')

# list templates and which devices they are associated with
template_url = "dataservice/template/device"

# list features that make up a template - warning: output too large for terminal, use postman
# template_feature_url = "dataservice/template/feature"

# list more deatils about specific features (as well as which device models are compatible) - warning: output too large for terminal, 
# use postman

# template_feature_url = "dataservice/template/feature/types"

template_response = sesh.get(url=f"{base_url}{template_url}", verify=False).json()
print(json.dumps(template_response, indent=2))
