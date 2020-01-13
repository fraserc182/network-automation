from getpass import getpass

ssh_pass = getpass("Enter ssh password: ")


## lab switches

lab_sw = {
    "device_type": "cisco_ios",
    "host": "test_lab_switch.blah",
    "username": "admin",
    "password": ssh_pass,
}



lab_switches = [
    lab_sw,
]