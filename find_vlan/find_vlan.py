
## import required modules
from pyntc import ntc_device as NTC
from ntc_templates.parse import parse_output
from getpass import getpass

## read the hosts text file
switches = open("./hosts_files/edge_switches.txt").read().splitlines()

## set user and ask for ssh password
ssh_user = "USERNAME"
ssh_pass = getpass()

## first loops through switches and runs show int status and gathers facts
for x in switches:
    switch = NTC(host=(x), username=(ssh_user), password=(ssh_pass), device_type='cisco_ios_ssh')
    show_int = switch.show('show int status')
    get_facts = switch.facts
    query_hostname = get_facts.get("hostname", "")
    print(query_hostname)
    print("")
    ## parses output into json arry so it can be worked with easier
    show_int_parsed = parse_output(platform="cisco_ios", command="show int status", data=show_int)
    ## loops through parsed interface output and checks for interfaces on vlan 12
    for i in show_int_parsed:
        if i['vlan'] == '12':
            intf = (i['port'])
            vlans = (i['vlan'])
            status = (i['status'])
            print('Found port '+intf, 'on VLAN ' +vlans, '& Port is: ' +status)