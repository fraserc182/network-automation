from getpass import getpass

def userchoice():
    print("Please choose what access level is required: ")
    print("")
    print ("1. readonly")
    print ("2. read/write")

while True:
    print("")
    userchoice()
    menuchoice = input("Enter your choice [1-2]: ")
    if menuchoice == '1':
        user = "ansible.user_ro"
        break
    elif menuchoice == '2':
        user = "ansible.user_rw"
        break
print("")
ssh_pass = getpass("Enter ssh password: ")

## edge switches

sw58 = {
    "device_type": "cisco_ios",
    "host": "edimanprswth058.pluk.eeghlan.net",
    "username": user,
    "password": ssh_pass,
}

sw56 = {
    "device_type": "cisco_ios",
    "host": "edimanprswth056.pluk.eeghlan.net",
    "username": user,
    "password": ssh_pass,
}

sw57 = {
    "device_type": "cisco_ios",
    "host": "edimanprswth057.pluk.eeghlan.net",
    "username": user,
    "password": ssh_pass,
}

sw59 = {
    "device_type": "cisco_ios",
    "host": "edimanprswth059.pluk.eeghlan.net",
    "username": user,
    "password": ssh_pass,
}

sw60 = {
    "device_type": "cisco_ios",
    "host": "edimanprswth060.pluk.eeghlan.net",
    "username": user,
    "password": ssh_pass,
}
sw61 = {
    "device_type": "cisco_ios",
    "host": "edimanprswth061.pluk.eeghlan.net",
    "username": user,
    "password": ssh_pass,
}

sw62 = {
    "device_type": "cisco_ios",
    "host": "edimanprswth062.pluk.eeghlan.net",
    "username": user,
    "password": ssh_pass,
}

sw66 = {
    "device_type": "cisco_ios",
    "host": "edimanprswth066.pluk.eeghlan.net",
    "username": user,
    "password": ssh_pass,
}

sw67 = {
    "device_type": "cisco_ios",
    "host": "edimanprswth067.pluk.eeghlan.net",
    "username": user,
    "password": ssh_pass,
}

sw68 = {
    "device_type": "cisco_ios",
    "host": "edimanprswth068.pluk.eeghlan.net",
    "username": user,
    "password": ssh_pass,
}

sw69 = {
    "device_type": "cisco_ios",
    "host": "edimanprswth069.pluk.eeghlan.net",
    "username": user,
    "password": ssh_pass,
}

sw74 = {
    "device_type": "cisco_ios",
    "host": "edimanprswth074.pluk.eeghlan.net",
    "username": user,
    "password": ssh_pass,
}

sw75 = {
    "device_type": "cisco_ios",
    "host": "edimanprswth075.pluk.eeghlan.net",
    "username": user,
    "password": ssh_pass,
}

sw76 = {
    "device_type": "cisco_ios",
    "host": "edimanprswth076.pluk.eeghlan.net",
    "username": user,
    "password": ssh_pass,
}

sw77 = {
    "device_type": "cisco_ios",
    "host": "edimanprswth077.pluk.eeghlan.net",
    "username": user,
    "password": ssh_pass,
}
sw78 = {
    "device_type": "cisco_ios",
    "host": "edimanprswth078.pluk.eeghlan.net",
    "username": user,
    "password": ssh_pass,
}

sw79 = {
    "device_type": "cisco_ios",
    "host": "edimanprswth079.pluk.eeghlan.net",
    "username": user,
    "password": ssh_pass,
}

sw80 = {
    "device_type": "cisco_ios",
    "host": "edimanprswth080.pluk.eeghlan.net",
    "username": user,
    "password": ssh_pass,
}

sw81 = {
    "device_type": "cisco_ios",
    "host": "edimanprswth081.pluk.eeghlan.net",
    "username": user,
    "password": ssh_pass,
}

sw82 = {
    "device_type": "cisco_ios",
    "host": "edimanprswth082.pluk.eeghlan.net",
    "username": user,
    "password": ssh_pass,
}

sw83 = {
    "device_type": "cisco_ios",
    "host": "edimanprswth083.pluk.eeghlan.net",
    "username": user,
    "password": ssh_pass,
}

sw84 = {
    "device_type": "cisco_ios",
    "host": "edimanprswth084.pluk.eeghlan.net",
    "username": user,
    "password": ssh_pass,
}

sw85 = {
    "device_type": "cisco_ios",
    "host": "edimanprswth085.pluk.eeghlan.net",
    "username": user,
    "password": ssh_pass,
}

sw86 = {
    "device_type": "cisco_ios",
    "host": "edimanprswth086.pluk.eeghlan.net",
    "username": user,
    "password": ssh_pass,
}

sw87 = {
    "device_type": "cisco_ios",
    "host": "edimanprswth087.pluk.eeghlan.net",
    "username": user,
    "password": ssh_pass,
}
sw90 = {
    "device_type": "cisco_ios",
    "host": "edimanprswth090.pluk.eeghlan.net",
    "username": user,
    "password": ssh_pass,
}

sw91 = {
    "device_type": "cisco_ios",
    "host": "edimanprswth091.pluk.eeghlan.net",
    "username": user,
    "password": ssh_pass,
}

sw92 = {
    "device_type": "cisco_ios",
    "host": "edimanprswth092.pluk.eeghlan.net",
    "username": user,
    "password": ssh_pass,
}

sw94 = {
    "device_type": "cisco_ios",
    "host": "edimanprswth094.pluk.eeghlan.net",
    "username": user,
    "password": ssh_pass,
}


## core switches

sw50 = {
    "device_type": "cisco_ios",
    "host": "edimanprswth050.pluk.eeghlan.net",
    "username": user,
    "password": ssh_pass,
}

sw51 = {
    "device_type": "cisco_ios",
    "host": "edimanprswth051.pluk.eeghlan.net",
    "username": user,
    "password": ssh_pass,
}

## server switches

sw72 = {
    "device_type": "cisco_ios",
    "host": "edimanprswth072.pluk.eeghlan.net",
    "username": user,
    "password": ssh_pass,
}

sw73 = {
    "device_type": "cisco_ios",
    "host": "edimanprswth073.pluk.eeghlan.net",
    "username": user,
    "password": ssh_pass,
}

sw52 = {
    "device_type": "cisco_ios",
    "host": "edimanprswth052.pluk.eeghlan.net",
    "username": user,
    "password": ssh_pass,
}

sw53 = {
    "device_type": "cisco_ios",
    "host": "edimanprswth053.pluk.eeghlan.net",
    "username": user,
    "password": ssh_pass,
}
## internet switches

sw48 = {
    "device_type": "cisco_ios",
    "host": "edimanprswth048.pluk.eeghlan.net",
    "username": user,
    "password": ssh_pass,
}

sw49 = {
    "device_type": "cisco_ios",
    "host": "edimanprswth049.pluk.eeghlan.net",
    "username": user,
    "password": ssh_pass,
}


## out of band switches

sw88 = {
    "device_type": "cisco_ios",
    "host": "edimanprswth088.pluk.eeghlan.net",
    "username": user,
    "password": ssh_pass,
}

sw89 = {
    "device_type": "cisco_ios",
    "host": "edimanprswth089.pluk.eeghlan.net",
    "username": user,
    "password": ssh_pass,
}

## storage switches

sw38 = {
    "device_type": "cisco_ios",
    "host": "edimanprswth038.pluk.eeghlan.net",
    "username": user,
    "password": ssh_pass,
}

sw39 = {
    "device_type": "cisco_ios",
    "host": "edimanprswth039.pluk.eeghlan.net",
    "username": user,
    "password": ssh_pass,
}

## lab switches

lab_sw_46 = {
    "device_type": "cisco_ios",
    "host": "edimandvswth046.lambienet.local",
    "username": "fraseradmin",
    "password": ssh_pass,
}

lab_sw_45 = {
    "device_type": "cisco_ios",
    "host": "edimandvswth045.lambienet.local",
    "username": "fraseradmin",
    "password": ssh_pass,
}






edge_switches = [
    sw58,
    sw56,
    sw57,
    sw59,
    sw60,
    sw61,
    sw62,
    sw66,
    sw67,
    sw68,
    sw69,
    sw74,
    sw75,
    sw76,
    sw77,
    sw78,
    sw79,
    sw80,
    sw81,
    sw82,
    sw83,
    sw84,
    sw85,
    sw86,
    sw87,
    sw90,
    sw91,
    sw92,
    sw94,
]

server_switches = [
    sw72,
    sw73,
    sw52,
    sw53
]

core_switches = [
    sw50,
    sw51,
]

internet_switches = [
    sw48,
    sw49,
]

oob_switches = [
    sw88,
    sw89,
]

storage_switches = [
    sw38,
    sw39,
]

lab_switches = [
    lab_sw_46,
    lab_sw_45
]