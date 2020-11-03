#!/usr/bin/env python
"""
Use processes and Netmiko to connect to each of the devices. Execute
'show version' on each device. Use a queue to pass the output back to the parent process.
Record the amount of time required to do this.
"""
from multiprocessing import Process, Queue

from datetime import datetime
from netmiko import ConnectHandler
from ntc_templates.parse import parse_output
from termcolor import colored, cprint
import sys
import time
from collections import Counter


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


def show_cisco_commands(a_device, output_q):
    """
    Use Netmiko to execute commands. Use a queue to pass the data back to
    the main process.
    """
    output_dict = {}
    remote_conn = ConnectHandler(**a_device)
    hostname = remote_conn.base_prompt
    sh_commands = remote_conn.send_command("show int status")
    sh_commands_parsed = parse_output(platform="cisco_ios", command="show int status", data=sh_commands)
    user_vlans = ['20', '22', '40', '43', '44', '45', '60']
    new_list = []

    for i in sh_commands_parsed:
        new_list.append(i['vlan'])

    print(hostname, + Counter(new_list))
        
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
        my_proc = Process(target=show_cisco_commands, args=(a_device, output_q))
        my_proc.start()
        procs.append(my_proc)

    # Make sure all processes have finished
    for a_proc in procs:
        a_proc.join()


    print("\nElapsed time: " + str(datetime.now() - start_time))


if __name__ == "__main__":
    main()
