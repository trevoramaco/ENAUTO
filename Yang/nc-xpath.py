from scrapli_netconf.driver import NetconfDriver

my_device = {
    "host": "10.10.21.15",
    "auth_username": "cisco",
    "auth_password": "cisco",
    "auth_strict_key": False,
    "port": 830
}

conn = NetconfDriver(**my_device)
conn.open()

# Everything up until this point was about establishing connection to device using scrapli

ospf_xpath = ''' /ospf-oper-data/ospf-state/ospf-instance[af="address-family-ipv4" and router-id="16843009"]
/ospf-area[area-id=0]/ospf-interface[name="GigabitEthernet2"]/ospf-neighbor[neighbor-id="2.2.2.2"]/state '''

response = conn.get(filter_=ospf_xpath, filter_type='xpath')
print(response.result)