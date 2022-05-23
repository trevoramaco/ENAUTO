import requests
import json

base_url = "https://dcloud-dnac-ctf-inst-rtp.cisco.com/dna/"
auth_endpoint = "system/api/v1/auth/token"

user = 'demo'
password = 'demo1234!'

auth_response = requests.post(url=f"{base_url}{auth_endpoint}", auth = (user, password))

token = auth_response.json()['Token']

headers = {
   "x-auth-token": token,
   "Accept": "application/json",
   "Content-Type": "application/json"
}


# we need the event ID's for assurnace IDs so we know what we can subscribe too
events_endpoint = "intent/api/v1/events?tags=ASSURANCE"

events_response = requests.get(url=f"{base_url}{events_endpoint}", headers=headers).json()

# print(json.dumps(events_response, indent=2))

# now we define a list of events we want to subscribe too
events_list = ["NETWORK-NON-FABRIC-WIRED-1-250", "NETWORK-DEVICES-3-207"]

payload = [
    {
        "name" : "trevor's subscription",
        "subscriptionEndpoints": [
            {
                "subscriptionDetails" : {
                    "connectorType" : "REST",
                    "name":"Azure function app",
                    "description":"ingest payload into CosmoDB",
                    "method":"POST",
                    "url":"https://something/app"
                }
            }
        ],
        "filter": {
            "eventIds": events_list
        }

    }
]

sub_endpoint = "intent/api/v1/event/subscription"

events_response = requests.post(url=f"{base_url}{sub_endpoint}", headers=headers, data=json.dumps(payload))

print(events_response.status_code)
print(events_response.text)