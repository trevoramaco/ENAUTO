from requests.exceptions import HTTPError
import requests, json

merakikey = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
base_url = "https://api.meraki.com/api/v1"

headers = {
    "X-Cisco-Meraki-API-Key": merakikey,
    "Content-Type": "application/json",
    "Accept": "application/json"
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

payload = {
    "name": "Long Island Office",
    "timeZone": "America/Los_Angeles",
    "tags": [ "tag1", "tag2" ],
    "notes": "Combined network for Long Island Office",
    "productTypes": [
        "appliance",
        "switch",
        "camera"
    ]
}

try:
    response = requests.post(url=f"{base_url}{endpoint}", headers=headers, data=json.dumps(payload))

    print(response.status_code)
    if response.status_code == 201:
        print(response.text)
except Exception as ex:
    print(ex)