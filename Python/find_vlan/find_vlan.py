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
from my_devices import lab_sw as devices
import sys
import time


def show_cisco_commands(a_device, output_q):
    """
    Use Netmiko to execute commands. Use a queue to pass the data back to
    the main process.
    """
    output_dict = {}
    remote_conn = ConnectHandler(**a_device)

    hostname = remote_conn.base_prompt ## this line pulls the hostname from the device

    ## these are the commands being sent to the devices
    sh_commands = remote_conn.send_command("show int status")
    sh_commands_parsed = parse_output(platform="cisco_ios", command="show int status", data=sh_commands)


    print(("=" * 80) + "\n")
    print((hostname))
    print("")

    ## this for loop looks for the information that is in in sh_commands_parsed variables
    for i in sh_commands_parsed:
        if i['vlan'] == '12':
            intf = (i['port'])
            vlans = (i['vlan'])
            status = (i['status'])
            print('Found port '+intf, 'on VLAN ' +vlans, "\n" 'Current Port status is: ' +status)
            print("")

    print("")
    print(("=" * 80) + "\n")
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
