# Cisco-Router-Automation
Automatically login into Cisco Router and perform pre-defined tasks.

03_3.9_paramiko.py:
This is a python code to login into cisco router using paramiko module.

04_3.9_paramiko_forloop.py:
This is a python code same as above but this has additional functionality to create interfaces automatically and add an IP to it also.

05_3.9_paramiko_forloop_device.py:
This python code allows you to login into two devices 1 by 1 and create interface and assign IP automatically.
Note: Router R3 has been added with IP 22.2.2.3/24 for this code.

Please refer my GNS3 and Kali VM setup screenshot to get the topology diagram.

Side Note: Only router R1 and Kali VM is required if you only want to run python codes.
           Router R2 and Internet NAT is used to connect the R2, R1 and Kali VM to internet through GNS3.
