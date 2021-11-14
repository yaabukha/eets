import subprocess
import os
import paramiko
from scp import SCPClient
import time




def stopCapture():
    try:
        # declare credentials
        #host = 'eets7302vm01.internal.cloudapp.net'
        host1 =  subprocess.getoutput('dig EETS7302VM01.internal.cloudapp.net +short')
        host2 =  subprocess.getoutput('dig EETS7302VM02.internal.cloudapp.net +short')
        username = 'eets7302'
        password = 'EETS@123'

        # connect to server
        con1 = paramiko.SSHClient()
        con1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        con1.load_system_host_keys()
        con1.connect(host1, username=username, password=password)
        transport1 = con1.get_transport()
        channel1 = transport1.open_session()
        con2 = paramiko.SSHClient()
        con2.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        con2.load_system_host_keys()
        con2.connect(host2, username=username, password=password)
        transport2 = con2.get_transport()
        channel2 = transport2.open_session()

        # copy the file accross
        with SCPClient(con1.get_transport()) as scp:
          scp.put('/home/eets7302/eets/testgit/remoteStop.py', '/home/eets7302/')

        channel1.exec_command('python3 /home/eets7302/remoteStop.py > /dev/null 2>&1 &')

        with SCPClient(con2.get_transport()) as scp:
          scp.put('/home/eets7302/eets/testgit/remoteStop.py', '/home/eets7302/')

        channel2.exec_command('python3 /home/eets7302/remoteStop.py > /dev/null 2>&1 &')


        # copy  he file accross
        with SCPClient(con1.get_transport()) as scp:
          scp.get('/home/eets7302/EETS7302VM01.pcap', '/home/eets7302/tempDownload/EETS7302VM01.pcap')
        with SCPClient(con2.get_transport()) as scp:
          scp.get('/home/eets7302/EETS7302VM02.pcap', '/home/eets7302/tempDownload/EETS7302VM02.pcap')

        time.sleep(2)
        cmd = 'zip /home/eets7302/tempDownload/captures.zip /home/eets7302/tempDownload/EETS7302VM01.pcap  /home/eets7302/tempDownload/EETS7302VM02.pcap'
        subprocess.Popen([cmd],shell=True)
        time.sleep(2)
        move = 'mv /home/eets7302/tempDownload/captures.zip /home/eets7302/uploads/captures.zip'
        subprocess.Popen([move],shell=True)


        return True
    except:
        return False
