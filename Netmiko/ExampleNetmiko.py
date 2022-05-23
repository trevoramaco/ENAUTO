from netmiko import ConnectHandler

router = {
    "device_type": "cisco_xe",
    "ip": "sandbox-iosxe-latest-1.cisco.com",
    "username": "developer",
    "password": "C1sco12345",
    "port": "8181",
}

try:
    c = ConnectHandler(**router)
    c.enable() # enter privallege mode
    response = c.send_command("show run")
    c.disconnect()
except Exception as e:
    print(e)
else:
    print(response)

