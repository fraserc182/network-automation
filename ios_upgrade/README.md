# ios_upgrade playbooks

This is composed of two scripts.
The first - copies an IOS image and verifies it's md5.
The second - sets boot path and reboots device then verifies it has upgraded successfully.

There are comments in each script explaining parts that need extra explanations.

ios_copy.yml
============================================

  vars: 
    compliant_ios_version: 15.2.4E8
    ios_md5: 2284cbaf62484a2689880b6a4eff7629
    file_name: c2960x-universalk9-mz.152-4.E8.bin
    scp_user: ansible_user

Set the ios version to whatever image you want to upgrade to, the md5 hash can be obtained from the cisco website.
The file_name variable should be the file name, not the file path.
scp_user should be set to a user that has rights to ssh onto the device. I have used the same user that the script is running under, which is set in your vars file.

In order of execution this script does the following:

* Gathers switch facts
* Checks if the device needs to be updated or not
* runs the show flash command and saves the output as a variable
* runs the show run command and saves the output as a variable
* debugs some commands for verification
* IF the image file already exists in flash THEN it verifies the md5 hash
* IF scp IS NOT enabled then the ip scp server enable command is executed
* IF the image file IS NOT present then uses scp command to copy file, verifies md5 hash then disables scp