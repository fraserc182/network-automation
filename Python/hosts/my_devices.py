from getpass import getpass

ssh_pass = getpass("Enter ssh password: ")


## lab switches

lab_sw = {
    "device_type": "cisco_ios",
    "host": "172.26.111.248",
    "username": "fraseradmin",
    "password": ssh_pass,
}



lab_switches = [
    lab_sw,
]