#!/usr/bin/env python

"""
Script to disable end user ports as defined by the user_vlans list.


The script runs in the following manner:

User selects which devices to work on, devices are held in my_devices.py

Use processes and Netmiko to connect to each of the devices. Execute
the commands defined in cisco_commands function on each device.
Use a queue to pass the output back to the parent process.

"""

from multiprocessing import Process, Queue
from datetime import datetime
from netmiko import ConnectHandler
from ntc_templates.parse import parse_output
import sys
import time

#! enter full path of where hosts file is located
sys.path.append('/root/fc_network_automation/python/hosts')


## List of vlans that are defined as end user vlans
user_vlans = ['20', '22', '40', '43', '44', '45', '60']

## Defines a menu so the user can choose which devices to work on
## Devices are defined within the my_devices.py file

def ciscoMenu():
    print("Please choose which device group to work on: ")
    print("")
    print ("1. Edge Switches")
    print ("2. Core Switches")
    print ("3. Internet Switches")
    print ("4. Out of Band Switches")
    print ("5. Server Switches")
    print ("6. Storage Switches")
    print ("7. Lab Switches")
    print ("8. Exit Program")

## This while loop displays the menu and when the user chooses an option
## It will import the required section of the my_devices.py file

while True:
    print("")
    ciscoMenu()
    menuchoice = input("Enter your choice [1-8]: ")
    if menuchoice == '1':
        from my_devices import edge_switches as devices
        break
    elif menuchoice == '2':
        from my_devices import core_switches as devices
        break
    elif menuchoice == '3':
        from my_devices import internet_switches as devices
        break
    elif menuchoice == '4':
        from my_devices import oob_switches as devices   
        break
    elif menuchoice == '5':
        from my_devices import server_switches as devices
        break
    elif menuchoice == '6':
        from my_devices import storage_switches as devices
        break
    elif menuchoice == '7':
        from my_devices import lab_switches as devices
        break
    elif menuchoice == '8':
        sys.exit("Goodbye!")
    else:
        input("\nInvalid option. Press Enter to try again..")


def cisco_commands(a_device, output_q):
    """
    Use Netmiko to execute commands. Use a queue to pass the data back to
    the main process.
    """

    output_dict = {}
    remote_conn = ConnectHandler(**a_device)
    hostname = remote_conn.base_prompt

    ## Runs the show interface status command on the connected device
    sh_commands = remote_conn.send_command("sh int status")

    ## Parses the output of the command into a dictionary so it can be worked with easier
    sh_commands_parsed = parse_output(platform="cisco_ios", command="sh int status", data=sh_commands)

    print("")
    print(hostname)
    print("")


    ## Opens/creates the modified_interfaces.csv file and tells it to append lines using the 'a' argument
    with open ('modified_interfaces.csv', 'a') as file:

        ## Loops through the parsed output of show interface status
        for i in sh_commands_parsed:

            ## if the vlan is in the user_vlans list and the status is either connected or notconnect
            ## then the ports shall be recorded in the csv and then shutdown
            if (i['vlan'] in user_vlans) and (i['status'] == 'connected' or i['status'] == 'notconnect'):
                intf = (i['port'])
                vlans = (i['vlan'])
                status = (i['status'])
                csv_var = hostname + ',' + intf
                file.write (csv_var + '\n')
                print('Found port '+intf, 'on VLAN ' +vlans, "\n" 'Current Port status is: ' +status, 
                "\n" 'Port will be shutdown')
                print("")
                config_commands = ['interface ' +intf,
                                   'shutdown']
                remote_conn.send_config_set(config_commands)

    output_q.put(output_dict)

def main():
    """
    Use processes and Netmiko to connect to each of the devices. Execute
    'show version' on each device. Use a queue to pass the output back to the parent process.
    Record the amount of time required to do this.
    """
    start_time = datetime.now()
    output_q = Queue(maxsize=35)

    procs = []
    for a_device in devices:
        my_proc = Process(target=cisco_commands, args=(a_device, output_q))
        my_proc.start()
        procs.append(my_proc)

    # Make sure all processes have finished
    for a_proc in procs:
        a_proc.join()


    print("\nElapsed time: " + str(datetime.now() - start_time))


if __name__ == "__main__":
    main()