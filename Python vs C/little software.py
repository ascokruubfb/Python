import time
def whomax():
    n1=6562
    n2=444
    n3=1515
    for i in range(3):
        who=max(n1,n2,n3)
        if who==n1:
            n1=0
        elif who==n2:
            n2=0
        elif who==n3:
            n3=0
        print(who)
def howmoney():
    print("jack is go bank 20$ one year is too money %3\n100 year last and jack dead\nso guys,what you think this?")
    x=20
    for i in range(100):
        x+=0.6
        print(str(i+1)+" year last >>> " + str(x)+"$")
def snakecrazy():
    z=""
    x=0
    for i in range(10000000):
        time.sleep(0.0010)
        z+=" "
        if(len(z)==100):
            z=""
        print(str(z)+"S")
sele=input("1.whomax\n2.howmoney\n3.snakecrazy\nplease select number:")
if sele==1:
    whomax()
elif sele==2:
    howmoney()
elif sele==3:
    snakecrazy()
