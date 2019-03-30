import tkinter
import tkinter.filedialog
root=tkinter.Tk()
root.geometry("400x500")
menubar=tkinter.Menu(root)
menuopen=tkinter.Menu(menubar,tearoff=0)
menubar.add_cascade(label="文件",menu=menuopen)
def openfile():
    way=tkinter.filedialog.askopenfilename(title="打开身份证数据", filetypes=[('文本文件', '*.txt')])
    x=open(way,"r")
    z=x.read()
    idtext.insert(0.1,z)
menuopen.add_command(label="载入数据",command=openfile)
root.config(menu=menubar)
def start():
    right.delete("1.0","end")
    idtext2=idtext.get("0.0","end")
    idtext3=idtext2.splitlines()
    idm = idtext3
    for i in range(len(idm)):
        id = idm[i]

        if(len(id)<17):
            right.insert(0.1,idm[i]+" 信息错误!\n")
        else:
            jyma = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
            idsx = []
            add = []
            pp = ""
            for i in range(17):
                idsx.insert(i, id[i])
                pp += idsx[i]
                a = int(idsx[i])
                b = int(jyma[i])
                add.append(a * b)
            number = int(add[0]) + int(add[1]) + int(add[2]) + int(add[3]) + int(add[4]) + int(add[5]) + int(add[6]) + int(
            add[7]) + int(add[8]) + int(add[9]) + +int(add[10]) + int(add[11]) + \
            int(add[12]) + int(add[13]) + int(add[14]) + int(add[15]) + int(add[16])
            know = number % 11
            key = {0: "1", 1: "0", 2: "X", 3: "9", 4: "8", 5: "7", 6: "6", 7: "5", 8: "4", 9: "3", 10: "2"}
            man = list(key.keys())
            woman = list(key.values())
            for i in range(11):
                if know == man[i]:
                    yep = pp + woman[i]
                    if (yep == id):
                        right.insert(0.1,id+" 通过国家身份数据库!\n")
                    else:
                        right.insert(0.1,id+" 身份信息错误!\n")


idtext=tkinter.Text(root,height="10")
idtext.pack()
tkinter.Button(root,text="开始校验",font=(30),command=start).place(x=155,y=142)
right=tkinter.Text(root,height="20")
right.place(y=180)
root.mainloop()
