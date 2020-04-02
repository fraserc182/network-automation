# find_vlan.py

When running this script ensure that the my_devices.py file is in the same directory or you have specified the absolute path to it when importing my_devices.
The my_devices file can be found in the hosts folder of this repository.

This script simply searches for information using the show interface status command and parsing it into a usuable format using ntc_templates.
It does this concurrently across all devices specified in the my_devices.py file using multiprocessing.

This is a simple template and can be used as a jumping off point for more complex tasks.