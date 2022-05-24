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

# create and add new admin user
# admin_endpoint = "dataservice/admin/user"

# payload = {
#     "group": ["netadmin"],
#     "description": "trevor's account",
#     "userName": "trevor",
#     "password": "password"
# }

# headers = {
#     "Accept": "application/json",
#     "Content-Type": "application/json",
# }

# response = sesh.post(url=f"{base_url}{admin_endpoint}", headers=headers, data=json.dumps(payload), verify=False)

# print(response.text)

# update password for account
pw_endpoint = "dataservice/admin/user/password/trevor"

payload ={
    "userName": "trevor",
    "password": "newpassword"
}

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
}

response = sesh.put(url=f"{base_url}{pw_endpoint}", headers=headers, data=json.dumps(payload), verify=False)

print(response.text)
