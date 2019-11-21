# network-automation

A repo containing some (hopefully) useful network automation scripts or jumping off points for your own scripts.

Updating IOS devices with Ansible
============================================
Within the ios_copy folder are two scripts to firstly copy over & verify the file and then perform a switch upgrade.
The reason why it is split up is because the scp command can take a long time to complete and I felt it better to split this into two scripts.