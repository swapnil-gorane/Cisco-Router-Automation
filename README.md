# Cisco-Router-Automation
Automatically login into Cisco Router and perform pre-defined tasks.

---- Windows 11 (Latest developement) ----

Python 3.10 codes will use my setup 4.jpg for topology. All routers in Windows 11.

01_3.10_telnet.py:
Starting the codes in Windows 11 now. Using GNS3, VM and Python codes in Windows 11.

---- End ----

---- Kali Linux ----

03_3.9_paramiko.py:
This is a python code to login into cisco router using paramiko module.

04_3.9_paramiko_forloop.py:
This is a python code same as above but this has additional functionality to create interfaces automatically and add an IP to it also.

05_3.9_paramiko_forloop_device.py:
This python code allows you to login into two devices 1 by 1 and create interface and assign IP automatically.

Note: Please refer GNS3 and Kali VM Topology V1 diagram for 05_3.9_paramiko_forloop_device.py.

Side Note: Only router R1 and Kali VM is required if you only want to run python codes.
           Router R2 and Internet NAT is used to connect the R2, R1 and Kali VM to internet through GNS3.
           
---- End ----
