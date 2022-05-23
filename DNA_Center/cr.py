import requests
import json

base_url = "https://sandboxdnac.cisco.com/dna/"
auth_endpoint = "system/api/v1/auth/token"

user = 'devnetuser'
password = 'Cisco123!'

auth_response = requests.post(url=f"{base_url}{auth_endpoint}", auth = (user, password))

token = auth_response.json()['Token']

headers = {
   "x-auth-token": token,
   "Accept": "application/json",
   "Content-Type": "application/json"
}

# first retrieve list of endpoints we are after
device_endpoint = "intent/api/v1/network_device?family=Switches and Hubs&type=Cisco Catalyst 9300 Switch"

dev_response = requests.get(url = f"{base_url}{device_endpoint}", headers=headers, verify=False).json()

print(json.dumps(dev_response, indent=2))

# iterate and sepperate ID from each device
device_ids = []
for device in dev_response['response']:
    device_id = device['id']
    device_ids.append(device_id)

payload = {
    "commands": [
        "show version"
    ],
    "deviceUuids": device_ids
}

command_endpoint = "intent/api/v1/network-device-poller/cli/read-request"

cli_response = requests.post(url=f"{base_url}{command_endpoint}", headers=headers, data=json.dumps(payload), verify=False)

print(cli_response.text)

# Unfortunantly, this won't work on read only sandbox, but return value from command runner endpoint looks like:
# { response: {"taskId":{}, "url": "stirng"}, "version": "string"}
# The taskID is the asynchronous task id, you can plug in task id in task API (like Get Task by ID method), response for this method 
# include paramater 'data' which is what you care about