import subprocess
import requests



def startCapture():
    try:
        hostName = subprocess.getoutput('hostname')
        fileName = hostName + ".pcap"
        subprocess.Popen(["sudo","tcpdump","-w",fileName])
        if hostName == "EETS7302VM01":
            startHttpRequest()
        return True
    except:
        return False

def startHttpRequest():
    url = "http://eets7302vm02.internal.cloudapp.net"
    for i in range(30):
        res = requests.get(url)





startCapture()
