# Connects to specified device and runs sh int status

from netmiko import ConnectHandler
from ntc_templates.parse import parse_output

cisco = { 
    'device_type': 'cisco_ios', 
    'host': '172.26.111.248', 
    'username': 'fraseradmin', 
    'password': 'Cr4ay0on5$', 
    }  

net_connect = ConnectHandler(**cisco) 

sh_int = net_connect.send_command("sh int status")

print(sh_int)