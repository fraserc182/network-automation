
## import required modules
from netmiko import ConnectHandler
from ntc_templates.parse import parse_output
from getpass import getpass

## read the hosts text file
switches = open("./hosts_files/edge_switches.txt").read().splitlines()

## set user and ask for ssh password
ssh_user = "ansible.user_ro"
ssh_pass = getpass()

## first loops through switches and runs show int status and gathers facts
for x in switches:
    switch = ConnectHandler(device_type='cisco_ios', host=(x), username=(ssh_user), password=(ssh_pass))
    show_int = switch.send_command("show int status")
    ## parses output so it can be worked with easier
    show_int_parsed = parse_output(platform="cisco_ios", command="show int status", data=show_int)
    ## pull hostname from running config
    sw_hostname = switch.send_command("show run | in hostname")
    sw_hostname = sw_hostname.split()
    hostname = sw_hostname[1]
    print(hostname)
    print("")
    
    ## loops through parsed interface output and checks for interfaces on vlan 12
    for i in show_int_parsed:
        if i['vlan'] == '12':
            intf = (i['port'])
            vlans = (i['vlan'])
            status = (i['status'])
            print('Found port '+intf, 'on VLAN ' +vlans, '& Port is: ' +status)