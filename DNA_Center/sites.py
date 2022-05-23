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

# lists all sites
sites_endpoint = "intent/api/v1/site"
# sites_response = requests.get(url=f"{base_url}{sites_endpoint}", headers=headers).json()['response']
#  print(json.dumps(sites_response, indent=2))

# lists current topology
topology_endpoint = "intent/api/v1/topology/site-topology"
top_response = requests.get(url = f"{base_url}{topology_endpoint}", headers=headers).json()['response']
print(json.dumps(top_response, indent=2))