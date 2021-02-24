import paramiko #library for ssh.
import time #this library is for sleep function, which is used for inducing some delay in seconds.
from getpass import getpass #getpass function from getpass library. 

ip = '22.2.2.1' #or use input('Enter IP: ') to get IP as input.
uname = 'cisco' #or use input('Enter Username: ') to get it as input.
pwd = 'cisco123' #or use input('Enter Password: ') to get it as input.

SESSION = paramiko.SSHClient() #SESSION is an object
SESSION.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #this command will neglect the trusted certificate 'SSHException' error.
SESSION.connect(ip,port=22,
                username=uname,
                password=pwd,
                look_for_keys=False,
                allow_agent=False) #indentation is given for asthestics only.

DEVICE_ACCESS = SESSION.invoke_shell() #invoking the shell
DEVICE_ACCESS.send(b'term length 0\n')
DEVICE_ACCESS.send(b'show run\n')
time.sleep(10) #2 seconds delay to generate output from above command and then display output.
output = DEVICE_ACCESS.recv(65000) #this will receive the data in single session
print(output.decode('ascii'))

SESSION.close #python recommends to close the session at the end.