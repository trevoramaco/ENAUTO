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

# build device template
create_template_url = "dataservice/template/device/feature"

# Within payload, there's lots of fields, but pay attention to generalTemplates: Lit of features we want to include 
# (where each ID comes from feature list we querried in other script)
payload = {
    "templateName": "vManage_template",
    "templateDescription": "vmanage demo",
    "deviceType": "vmanage",
    "configType": "template",
    "factoryDefault": False,
    "policyId": "",
    "featureTemplateUidRange": [],
    "generalTemplates": [
        {
            "templateId": "476b52d0-3196-4625-82be-1deb124a5199",
            "templateType": "aaa"
        },
        {
            "templateId": "777f1262-1ae7-4dea-82d1-b24b2132d548",
            "templateType": "system-vedge"
        },
        {
            "templateId": "bf3fcac8-8ab3-46a3-9ab5-c0d3e6107826",
            "templateType": "vpn-vsmart"
        },
    ]
}

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# response = sesh.post(url=f"{base_url}{create_template_url}", headers=headers, data= json.dumps(payload)).json()
# print(json.dumps(response, indent=2))

# You should get a templateID returned which you can use (I can't figure out postman...)

templateID = '000000-000000-0000-0000'

# deviceID comes from inventory calls and is the device you want to attach the template too (you can attach to multiple), 
# grab the uuid field!
device_temp_payload = {
    "templateId" : templateID,
    "deviceIDs" : ["81ac6722-a226-4411-9d5d-45c0ca7d567b"],
    "isEdited": False,
    "isMasterEdited": False
}

# Attach device template to devices
device_temp_url = "dataservice/template/device/config/input"

response = sesh.post(url=f"{base_url}{device_temp_url}", headers=headers, data=json.dumps(device_temp_payload), verify=False)