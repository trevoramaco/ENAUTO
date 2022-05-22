import requests
import json

router = {
    "host": "sandbox-iosxe-recomm-1.cisco.com",
    "port": "443",
    "username": "developer",
    "password": "C1sco12345"
}

url = f"https://{router['host']}:{router['port']}/restconf/data/netconf-state/capabilities"

headers = {
    "Accept":"application/yang-data+json",
    "Content-Type":"application/yang-data+json"
}

response = requests.get(url=url, headers=headers, auth=(router['username'], router['password']), verify=False)

if response.status_code == 200:
    response_dict = response.json()

    for capability in response_dict['ietf-netconf-monitoring:capabilities']['capability']:
        print(capability)