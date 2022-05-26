from requests.exceptions import HTTPError
import requests, json

merakikey = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"

base_url = "https://api.meraki.com/api/v1"

headers = {
    "X-Cisco-Meraki-API-Key": merakikey
}

# get list of orgs and information
endpoint = "/organizations"

try:
    response = requests.get(url=f"{base_url}{endpoint}", headers=headers)
    if response.status_code == 200:
        orgs = response.json()
        for org in orgs:
            if org['name'] == 'DevNet Sandbox':
                orgid = org['id']
except Exception as ex:
    print(ex)

# get a list of networks in org
endpoint = f"/organizations/{orgid}/networks"

try:
    response = requests.get(url=f"{base_url}{endpoint}", headers=headers)
    if response.status_code == 200:
        nets = response.json()
        for net in nets:
            if net['name'] == 'DNSMB3':
                netid = net['id']
except HTTPError as http:
    print(http)
except Exception as ex:
    print(ex)


# get a list of devices in network
endpoint = f"/networks/{netid}/devices"

try:
    response = requests.get(url=f"{base_url}{endpoint}", headers=headers)
    if response.status_code == 200:
        devices = response.json()
        for device in devices:
            print(device)
except HTTPError as http:
    print(http)
except Exception as ex:
    print(ex)