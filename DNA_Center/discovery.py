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

# you need the credentials for ssh and/or snmp before you can do a device discovery/interact with all these devices
# cli
cred_cli_endpoint = "intent/api/v1/global-credential?credentialSubType=CLI"

cli_response = requests.get(url=f"{base_url}{cred_cli_endpoint}", headers=headers).json()['response'][0]
print(cli_response)
cli_cred = cli_response['id']

# snmp
cred_snmp_endpoint = "intent/api/v1/global-credential?credentialSubType=SNMP_WRITE_COMMUNITY"

snmp_response = requests.get(url=f"{base_url}{cred_snmp_endpoint}", headers=headers).json()['response'][0]
print(snmp_response)
snmp_cred = snmp_response['id']


# device dicovery payload (specify IP range method for discovery) and call
paylod = {
    "name" : "trevor's discovery",
    "discoveryType" : "Range",
    "ipAddressList" : "10.10.20.30-10.10.10.254",
    "protocolOrder" : "ssh,telnet",
    "preferredMgmtIpMethod" : "",
    "globalCredentialList" : [cli_cred, snmp_cred]
}

discovery_endpoint = "intent/api/v1/discovery"

disc_response = requests.post(url=f"{base_url}{discovery_endpoint}", headers=headers, data=json.dumps(paylod))
print(disc_response)
print(disc_response.text)

# method not supported in snadbox, but similar return to command runner, take the returned task id and plug it into network discovery 
# methods to access data