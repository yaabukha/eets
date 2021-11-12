import subprocess 
import os




def stopCapture():
    try:
        Pid = subprocess.getoutput('ps -e | pgrep tcpdump | grep -v grep')
        if Pid !="":
          os.system('sudo kill -2 ' +  str(Pid))
        
        return True
    except:
        return False

stopCapture()
