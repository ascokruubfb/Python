# -*- coding:GBK -*-
class system():
    def start(self):
       print("Welcome used this calculator！\nand this is digital command:\n1.check version\n2.add\n3.minus\n4.multiply\n5.except\n6.quit")
       command = input("please entry command:")
       if int(command)==1:
           self.ver()
       elif int(command)==2:
           self.jia()
       elif int(command)==3:
           self.jian()
       elif int(command)==4:
           self.cheng()
       elif int(command)==5:
           self.chu()
       elif int(command)==6:
           self.exit()
       else:
           print("the program itself can not search your command!")
           input()
           self.start()

    def ver(self):
        print("calculator ver 3.0")
        input()
        self.start()
    def jia(self):
        one=input("ADD:")
        two=input("ADD 2:")
        print("success to ："+str(int(one)+int(two)))
        input()
        self.start()
    def jian(self):
        one=input("minus:")
        two=input("minus:")
        print("success to："+str(int(one)-int(two)))
        input()
        self.start()
    def cheng(self):
        one=input("multiply:")
        two=input("multiply2:")
        print("success to："+str(int(one)*int(two)))
        input()
        self.start()
    def chu(self):
        one=input("except:")
        two=input("except2:")
        print("success to："+str(int(one)//int(two)))
        input()
        self.start()
    def exit(self):
        print("Good bye,wish you happy one day. press entry end~")
        input()
        quit()

system=system()
system.start()
