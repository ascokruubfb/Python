import tkinter
import tkinter.messagebox as msg
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
windows=tkinter.Tk()
windows.geometry("300x550")
windows.title("SSH连接软件")
tkinter.Label(windows,text="SSH ADDRESS ",font=(25)).place(x=20,y=20)
tkinter.Label(windows,text="SSH USERNAME ",font=(25)).place(x=20,y=60)
tkinter.Label(windows,text="SSH PASSWORD ",font=(25)).place(x=20,y=100)
tkinter.Label(windows,text="SSH PORT ",font=(25)).place(x=20,y=140)
a=tkinter.Entry(windows,font=(20))
a.place(x=120,y=25)
b=tkinter.Entry(windows,font=(20))
b.place(x=120,y=65)
c=tkinter.Entry(windows,font=(20))
c.place(x=120,y=105)
e=tkinter.Entry(windows,font=(20))
e.place(x=120,y=145)

shell=tkinter.Text(windows,height=20,width=42,bg="black",fg="red")
shell.place(x=1,y=230)

def sshx():
    global ssh
    ssh.connect(a.get(), e.get(), b.get(),c.get())
    stdin, stdout, stderr = ssh.exec_command('ls')
    result=stdout.read().decode()
    shell.insert("insert",result)
    abs=shell.get(1.0,"end")
    if abs == "" :
        msg.showerror("错误","此连接不通，或账户密码错误！")
    else:
        msg.showinfo("hacker~","success!")

d=tkinter.Button(windows,text="Connect Line",width="15",height="2",command=sshx)
d.place(x=145,y=175)
def sshe():
    global ssh
    stdin, stdout, stderr = ssh.exec_command(textshell.get())
    result=stdout.read().decode()
    shell.insert("insert",result)
textshell = tkinter.Entry(windows,font=(30))
textshell.place(x=110,y=505)
shellgo=tkinter.Button(windows,text="Shell go",width="15",height="2",command=sshe)
shellgo.place(x=5,y=500)
windows.mainloop()
