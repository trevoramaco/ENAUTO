from ncclient import manager
from router_info import router

config_template = open("/Users/tmaco/Documents/Training & Certifications/Certifications/CCNP/ENAUTO/ENAUTO/Netconf/ios_config.xml").read()

netconf_config = config_template.format(interface_name="GigabitEthernet2", interface_desc="daniyal")

with manager.connect(**router, hostkey_verify=False) as m:
    response = m.edit_config(netconf_config, target="running")

print(response)