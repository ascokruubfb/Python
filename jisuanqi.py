import tkinter as tk
import tkinter.messagebox as msg
num1=""
a="0"
window = tk.Tk()
window.title("简易计算器")
window.geometry("190x250")
entry=tk.Entry(window,width=50,font=(50))
entry.pack()
def one():
   how=entry.get()
   entry.insert(len(how),1)
def two():
   how=entry.get()
   entry.insert(len(how),2)
def three():
   how=entry.get()
   entry.insert(len(how),3)
def four():
   how=entry.get()
   entry.insert(len(how),4)
def five():
   how=entry.get()
   entry.insert(len(how),5)
def six():
   how=entry.get()
   entry.insert(len(how),6)
def seven():
   how=entry.get()
   entry.insert(len(how),7)
def eight():
   how=entry.get()
   entry.insert(len(how),8)
def nine():
   how=entry.get()
   entry.insert(len(how),9)
def zero():
   how=entry.get()
   entry.insert(len(how),0)
def jia():
   global num1
   global a
   a="0"
   num1=entry.get()
   entry.delete(0,300)
def jian():
   global num1
   global a
   a="1"
   num1=entry.get()
   entry.delete(0,300)
def cheng():
   global num1
   global a
   a="2"
   num1=entry.get()
   entry.delete(0,300)
def chu():
   global num1
   global a
   a="3"
   num1=entry.get()
   entry.delete(0,300)

def dy():
   global a
   if a=="0":
      msg.showinfo("计算成功",str(num1)+" 加上 "+str(entry.get())+" 结果于:"+str(int(num1)+int((entry.get()))))
      entry.delete(0,300)
   elif a=="1":
      msg.showinfo("计算成功",str(num1)+" 减去 "+str(entry.get())+" 结果于:"+str(int(num1)-int((entry.get()))))
      entry.delete(0,300)
   elif a=="2":
      msg.showinfo("计算成功",str(num1)+" 乘以 "+str(entry.get())+" 结果于:"+str(int(num1)*int((entry.get()))))
      entry.delete(0,300)
   elif a=="3":
      msg.showinfo("计算成功",str(num1)+" 除以 "+str(entry.get())+" 结果于:"+str(int(num1)//int((entry.get()))))
      entry.delete(0,300)
tk.Button(window,text="one",width=8,height=2,command=one).place(x=1,y=54)
tk.Button(window,text="two",width=8,height=2,command=two).place(x=65,y=54)
tk.Button(window,text="one",width=8,height=2,command=three).place(x=130,y=54)
tk.Button(window,text="two",width=8,height=2,command=four).place(x=1,y=91)
tk.Button(window,text="five",width=8,height=2,command=five).place(x=65,y=91)
tk.Button(window,text="six",width=8,height=2,command=six).place(x=130,y=91)
tk.Button(window,text="seven",width=8,height=2,command=seven).place(x=1,y=130)
tk.Button(window,text="eight",width=8,height=2,command=eight).place(x=65,y=130)
tk.Button(window,text="nine",width=8,height=2,command=nine).place(x=130,y=130)
tk.Button(window,text="zero",width=8,height=2,command=zero).place(x=65,y=170)
tk.Button(window,text="+",width=8,height=2,command=jia).place(x=1,y=170)
tk.Button(window,text="=",width=8,height=2,fg="green",command=dy).place(x=130,y=170)
tk.Button(window,text="-",width=8,height=2,command=jian).place(x=1,y=210)
tk.Button(window,text="*",width=8,height=2,command=cheng).place(x=65,y=210)
tk.Button(window,text="/",width=8,height=2,command=chu).place(x=130,y=210)
tk.Label(text="PYTHON简易计算器",font=(60),fg="red",bg="black").place(x=1,y=27)
window.mainloop()
