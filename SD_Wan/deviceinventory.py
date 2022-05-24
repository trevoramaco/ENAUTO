import requests
import json
import sys

# Authentication to sd-wan uses request sessions: endpoint, username, and password must be specified with special 'j_*' format
base_url = "https://sandbox-sdwan-2.cisco.com/"
auth_endpoint = "j_security_check"

login_body = {
    "j_username": "devnetuser",
    "j_password": "RG!_Yw919_83"
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

# list all devices
device_endpoint = "dataservice/device"

# list only vedges (more verbose output)
# device_vedges_endpoint = "dataservice/system/device/vedges"

# list high level status of all devices
# device_status_endpoint = "dataservice/device/monitor"

device_response = sesh.get(url=f"{base_url}{device_endpoint}", verify=False).json()

print(json.dumps(device_response, indent=2))
