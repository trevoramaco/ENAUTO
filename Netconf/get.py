from ncclient import manager
# import logging
import xmltodict

# logging.basicConfig(level=logging.DEBUG)

router = {
    "host": "sandbox-iosxe-recomm-1.cisco.com",
    "port": "830",
    "username": "developer",
    "password": "C1sco12345"
}

int_filter = """
<filter>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>GigabitEthernet2</name>
    </interface>
  </interfaces>
  <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>GigabitEthernet2</name>
    </interface>
  </interfaces-state>
</filter>
"""

with manager.connect(**router, hostkey_verify=False) as m:
    netconf_response = m.get(int_filter)

python_response = xmltodict.parse(netconf_response.xml)["rpc-reply"]["data"] # remove top level message and operation tags

# Seperate out 2 yang models returned in response
op = python_response["interfaces-state"]["interface"] 
config = python_response["interfaces"]["interface"]

print(f"Name: {config['name']['#text']}")
print(f"Packets In: {op['statistics']['in-unicast-pkts']}")