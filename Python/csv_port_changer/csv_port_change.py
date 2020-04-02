#!/usr/bin/env python

'''
Takes input from the port_change.csv file and will run through all interfaces updating their
description and vlans to what is specified in the csv.
'''

from multiprocessing import Process, Queue
from datetime import datetime
from netmiko import ConnectHandler
from ntc_templates.parse import parse_output
import csv
from getpass import getpass

ssh_pass = getpass("Enter ssh password: ")
allowed_vlans = ['20', '22', '40', '43', '44', '45', '60']

## commands that will be passed to the device
## arguments are pased in by the main function and the my_proc variable
def cisco_commands(a_device, output_q, desc, intf, vlan):
    """
    Use Netmiko to execute commands. Use a queue to pass the data back to
    the main process.
    """
    
    output_dict = {}
    remote_conn = ConnectHandler(**a_device)
    hostname = remote_conn.base_prompt

    ## commands to be ran on device
    config_commands = ([ 'interface '+ intf, 
                    'switchport access vlan '+ vlan, 
                    'description '+ desc ])
    
    ## runs the show interface status command on the device
    sh_commands = remote_conn.send_command("sh int "+intf+ " status")
    ## uses ntc_template to parse the command output into a dictionary which can be easily worked with
    sh_commands_parsed = parse_output(platform="cisco_ios", command="sh int status", data=sh_commands)

    ## loop through the parsed output
    for i in sh_commands_parsed:
        ## checks if the vlan is in the allowed_lists list & runs config_commands if it is
        if i['vlan'] in allowed_vlans:
            remote_conn.send_config_set(config_commands)
            print("=" * 60 + "\n")
            print(hostname+ ' ' +intf)
            print("")
            print(config_commands)
            print("=" * 60 + "\n")
        else:
        ## otherwise it will print the below message and show the port config so it can be understood why it failed
            print("=" * 60 + "\n")
            print(hostname+ ' ' +intf)
            print("")
            print("VLAN not allowed or switchport is trunk. \nCurrent port configuration: "+i['vlan'])
            print("=" * 60 + "\n")            

    output_q.put(output_dict)



def main():
    start_time = datetime.now()
    output_q = Queue(maxsize=20)

    procs = []

    ## opens the csv file containing the required info
    with open('port_change.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                ", ".join(row)
                line_count += 1
            line_count += 1
            ## pulls out the desired info from the csv and passes them to variables
            hostname = row["hostname"]
            desc = row["description"]
            port = row["interface"]
            desired_vlan = row["vlan"]
            ## creates the connection dictionary with some of the variables
            cisco = {
                'device_type': 'cisco_ios',
                'host': hostname,
                'username': 'USERNAME',
                'password': ssh_pass,
                }
            ## passes the arguments to the cisco_commands function
            my_proc = Process(target=cisco_commands, args=(cisco, output_q, desc, port, desired_vlan))
            my_proc.start()
            procs.append(my_proc)

    # Make sure all processes have finished
    for a_proc in procs:
        a_proc.join()


    print("\nElapsed time: " + str(datetime.now() - start_time))


if __name__ == "__main__":
    main()