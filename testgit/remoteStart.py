import subprocess
import requests



def startCapture():
    try:
        hostName = subprocess.getoutput('hostname')
        fileName = hostName + ".pcap"
        subprocess.Popen(["sudo","tcpdump","-w",fileName])
       
        return True
    except:
        return False







startCapture()
