import tkinter
import tkinter.filedialog
import xlrd
import xlwt
import tkinter.messagebox as msg
root=tkinter.Tk() #载入TK
xlsxname=[]
xlsxid=[]
xlsxyn=[]
def clear():
    global xlsxid
    global xlsxname
    xlsxid=[]
    xlsxname=[]
namekey=0
idkey=0
root.title("身份证验证系统")
root.geometry("400x480") #设置大小
menubar=tkinter.Menu(root) #创建菜单
menuopen=tkinter.Menu(menubar,tearoff=0) #归属主菜单
menubar.add_cascade(label="文件",menu=menuopen) #创建主菜单
def openfile(): #打开一个文件
    clear()
    way=tkinter.filedialog.askopenfilename(title="打开身份证数据", filetypes=[('文本文件', '*.txt')])
    x=open(way,"r")
    z=x.read()
    idtext.delete("1.0","end")
    idtext.insert("end",z)

def openxlsx():
    global xlsxname
    global xlsxid
    if idkey==0:
        msg.showinfo("打开失败","未经选择key，不可导入")
    else:
        xlsxyn.insert(0,"校验结果")
        xlsx=tkinter.filedialog.askopenfilename(title="打开xlsx数据", filetypes=[('xlsx文件', '*.xlsx')])
        data=xlrd.open_workbook(xlsx)
        sheet=data.sheet_by_index(0)
        name=sheet.col_values(namekey)
        id=sheet.col_values(idkey)
        xlsxname=name
        xlsxid=id
        idtext.delete("1.0","end")
        for i in range(len(id)):
            idtext.insert("end",id[i]+"\n")
def savexlsx():
    lujing=tkinter.filedialog.asksaveasfilename(title="保存xlsx数据", filetypes=[("xlsx",'.xlsx')])
    wbk = xlwt.Workbook()
    sheet=wbk.add_sheet("校验完成数据")
    for i in range(len(xlsxid)):
       sheet.write(i,0,xlsxname[i])
       sheet.write(i,1,xlsxid[i])
       sheet.write(i,2,xlsxyn[i])
    wbk.save(str(lujing)+".xlsx")
    msg.showinfo("保存成功","数据已经保存")
menuopen.add_command(label="载入数据",command=openfile)#调用函数
menuopen.add_command(label="打开xlsx",command=openxlsx)#调用函数
menuopen.add_command(label="保存xlsx",command=savexlsx)#调用函数
root.config(menu=menubar) #配置菜单 不用说了
def start(): #核心代码
    right.delete("1.0","end") #载入清空文本框2
    idtext2=idtext.get("0.0","end") #获取文本框1
    idtext3=idtext2.splitlines() #分割文本框、
    idm = idtext3 #变了载入分割的数据
    for i in range(len(idm)): #循环匹配身份证
        id = idm[i] #变量置入
        if(len(id)<17): #小于18位不是真正的身份证
            right.insert(0.1,idm[i]+" 信息错误!\n")
        else:
            jyma = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2] #验证身份证关键的key
            idsx = [] #置入身份证数据
            add = []
            pp = ""
            number=0
            for i in range(17): #循环十七次表示18位身份证
                idsx.insert(i, id[i]) #加入ID数据
                pp += idsx[i] #转换成文本 方便以后相加于最后一位数
                a = int(idsx[i]) #身份证的数据
                b = int(jyma[i]) #身份证验证的key
                add.append(a * b) #相乘到add变量
                number += int(add[i]) #相加相加

            know = number % 11 #取摸
            key = {0: "1", 1: "0", 2: "X", 3: "9", 4: "8", 5: "7", 6: "6", 7: "5", 8: "4", 9: "3", 10: "2"} #字典为匹配身份证最后一位
            man = list(key.keys()) #man 列出键值
            woman = list(key.values()) #woman 列出数值
            for i in range(11):  #循环11次位数值的匹配
                if know == man[i]: #匹配指定的数字到键值后等成于数值
                    yep = pp + woman[i] #身份证整数字
                    if (yep == id): #被处理的身份证数字如果等于载入的数字
                        right.insert("end",id+" 通过国家身份数据库!\n") #则正确
                        xlsxyn.append("正确")
                    else:
                        right.insert("end",id+" 身份信息错误!\n") #则错误
                        xlsxyn.append("错误")
idtext=tkinter.Text(root,height="10")
idtext.pack()
tkinter.Button(root,text="开始校验",font=(30),command=start).place(x=155,y=142)
right=tkinter.Text(root,height="20")
right.place(y=180)
tkinter.Label(root,text="col key 1").place(x=2,y=450)
namekeytext=tkinter.Entry(root,width=5)
namekeytext.place(x=60,y=450)
tkinter.Label(root,text="col key 2").place(x=90,y=450)
idkeytext=tkinter.Entry(root,width=5)
idkeytext.place(x=150,y=450)
def set():
    global namekey
    global idkey
    if namekeytext.get()=="":
        msg.showinfo("提示","请输入name key")
    elif idkeytext.get()=="":
        msg.showinfo("提示","请输入id key")
    else:
        namekey=int(namekeytext.get())
        idkey=int(idkeytext.get())
        msg.showinfo("提示","KEY 锁定完毕，需要修改请自行输入。")
tkinter.Button(root,text="lock that",command=set).place(x=190,y=448)
root.mainloop()
