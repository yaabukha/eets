import subprocess
import paramiko
from scp import SCPClient




def startCapture():
    try:
        host1 =  subprocess.getoutput('dig EETS7302VM01.internal.cloudapp.net +short')
        host2 =  subprocess.getoutput('dig EETS7302VM02.internal.cloudapp.net +short')
        username = 'eets7302'
        password = 'EETS@123'
        #connect to server
        con1 = paramiko.SSHClient()
        con1.load_system_host_keys()
        con1.connect(host1, username=username, password=password)
        con2 = paramiko.SSHClient()
        con2.load_system_host_keys()
        con2.connect(host2, username=username, password=password)
        transport1 = con1.get_transport()
        channel1 = transport1.open_session()
        transport2 = con2.get_transport()
        channel2 = transport2.open_session()

        # copy the file accross
        with SCPClient(con1.get_transport()) as scp:
         scp.put('/home/eets7302/eets/testgit/remoteStart.py', '/home/eets7302/')

         channel1.exec_command('python3 /home/eets7302/remoteStart.py > /dev/null 2>&1 &')
        with SCPClient(con2.get_transport()) as scp:
         scp.put('/home/eets7302/eets/testgit/remoteStart.py', '/home/eets7302/')

         channel2.exec_command('python3 /home/eets7302/remoteStart.py > /dev/null 2>&1 &')    



        return True
    except:
        return False
