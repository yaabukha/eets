import subprocess
import os
import paramiko
from scp import SCPClient





def stopCapture():
    try:
        # declare credentials
        #host = 'eets7302vm01.internal.cloudapp.net'
        host =  subprocess.getoutput('dig EETS7302VM01.internal.cloudapp.net +short')
        username = 'eets7302'
        password = 'EETS@123'

        # connect to server
        con = paramiko.SSHClient()
        con.load_system_host_keys()
        con.connect(host, username=username, password=password)
        transport = con.get_transport()
        channel = transport.open_session()

        # copy the file accross
        with SCPClient(con.get_transport()) as scp:
          scp.put('/home/eets7302/eets/testgit/remoteStop.py', '/home/eets7302/')

        channel.exec_command('python3 /home/eets7302/remoteStop.py > /dev/null 2>&1 &')




        # copy  he file accross
        with SCPClient(con.get_transport()) as scp:
          scp.get('/home/eets7302/EETS7302VM01.pcap', '/home/eets7302/uploads/EETS7302VM01.pcap')


        cmd = 'zip /home/eets7302/uploads/captures.zip /home/eets7302/uploads/EETS7302VM01.pcap'
        subprocess.Popen([cmd],shell=True)


        return True
    except:
        return False
