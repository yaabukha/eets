import subprocess
import paramiko   
from scp import SCPClient   
   
# declare credentials   
host = '10.22.1.4'   
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
    scp.put('/home/eets7302/eets/testgit/remoteStart.py', '/home/eets7302/')   

channel.exec_command('python3 /home/eets7302/remoteStart.py > /dev/null 2>&1 &')



def startCapture():
    try:
        hostName = subprocess.getoutput('hostname')
        fileName = hostName + ".pcap"
        subprocess.Popen(["sudo","tcpdump","-w",fileName])
        return True
    except:
        return False


startCapture()