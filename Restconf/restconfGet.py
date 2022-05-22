
import requests
import json

router = {
    "host": "sandbox-iosxe-recomm-1.cisco.com",
    "port": "443",
    "username": "developer",
    "password": "C1sco12345"
}

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

# url = f"https://{router['host']}:{router['port']}/restconf/data/ietf-routing:routing"

# response = requests.get(url=url, headers=headers, auth=(
#     router['user'], router['password']), verify=False).json()

# print(json.dumps(response, indent=2))

url = f"https://{router['host']}:{router['port']}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/"

response = requests.get(url=url, headers=headers, auth=(
    router['username'], router['password']), verify=False).json()

print(json.dumps(response, indent=2))
