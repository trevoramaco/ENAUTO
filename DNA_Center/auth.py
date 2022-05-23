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

print(token)