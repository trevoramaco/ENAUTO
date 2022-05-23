from netmiko import ConnectHandler

router = {
    "device_type": "cisco_xe",
    "ip": "sandbox-iosxe-latest-1.cisco.com",
    "username": "developer",
    "password": "C1sco12345",
    "port": "8181",
}

configs = ['int lookback101', 'ip address 10.99.98.1 255.255.255.0', 'no shut'] # list of commands to execute ('conf t' not included because this is done automatically)

try:
    c = ConnectHandler(**router)
    c.enable() # enter privallege mode
    c.send_config_set(configs)
    response = c.send_command('show ip int b')
    c.disconnect()
except Exception as e:
    print(e)
else:
    print(response)

