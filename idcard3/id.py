import tkinter
import tkinter.filedialog
import xlrd
import xlwt
import tkinter.messagebox as msg

root = tkinter.Tk()  # 载入TK
xlsxname = []
xlsxid = []
xlsxyn = []


def clear():
    global xlsxid
    global xlsxname
    xlsxid = []
    xlsxname = []


namekey = 0
idkey = 0
root.title("身份证验证系统")
root.geometry("400x490")  # 设置大小
menubar = tkinter.Menu(root)  # 创建菜单
menuopen = tkinter.Menu(menubar, tearoff=0)  # 归属主菜单
menubar.add_cascade(label="txt文件", menu=menuopen)  # 创建主菜单
menuopenxl = tkinter.Menu(menubar, tearoff=0)  # 归属主菜单
menubar.add_cascade(label="Excel文件", menu=menuopenxl)  # 创建主菜单
allright = tkinter.Menu(menubar, tearoff=0)  # 归属主菜单
menubar.add_cascade(label="关于软件", menu=allright)  # 创建主菜单
root.resizable(0, 0)
root.iconbitmap("idcard.ico")


def root2():
    root2 = tkinter.Toplevel()
    root2.title("软件信息以及开发过程")
    root2.geometry("300x400")
    root2.resizable(0, 0)
    canva=tkinter.Canvas(root2,width=300,height=400,bg="green")\

    tkinter.Label(root2,text="本程序由微机一班某同学开发",font=(25),fg="white",bg="green").place(x=50,y=2)
    tkinter.Label(root2,text="本程序由微机一班同学开发，由python\n语言编写，为了程序的支持，您可以进行\n微信维码扫描红包打赏！",font=(15),fg="white",bg="green").place(x=2,y=30)
    image_file=tkinter.PhotoImage(file="das.gif")
    canva.create_image(18,100,anchor="nw",image=image_file)

    canva.pack()
    root2.mainloop()


allright.add_command(label="软件信息", command=root2)


def openfile():  # 打开一个文件
    clear()
    way = tkinter.filedialog.askopenfilename(title="打开身份证数据", filetypes=[('文本文件', '*.txt')])
    x = open(way, "r")
    z = x.read()
    idtext.delete("1.0", "end")
    idtext.insert("end", z)


def openxlsx():
    set()
    global xlsxname
    global xlsxid
    if idkey == 0:
        msg.showinfo("打开失败", "未经选择列，不可导入")
    else:
        xlsx = tkinter.filedialog.askopenfilename(title="打开xlsx数据", filetypes=[('xlsx文件', '*.xlsx')])
        data = xlrd.open_workbook(xlsx)
        sheet = data.sheet_by_index(0)
        name = sheet.col_values(namekey - 1)
        id = sheet.col_values(idkey - 1)
        xlsxname = name
        xlsxid = id
        idtext.delete("1.0", "end")
        for i in range(len(id)):
            idtext.insert("end", id[i] + "\n")


def savexlsx():
    lujing = tkinter.filedialog.asksaveasfilename(title="保存xlsx数据", filetypes=[("xlsx", '.xlsx')])
    wbk = xlwt.Workbook()
    sheet = wbk.add_sheet("校验完成数据")
    for i in range(len(xlsxid)):
        sheet.write(i, 0, xlsxname[i])
        sheet.write(i, 1, xlsxid[i])
        sheet.write(i, 2, xlsxyn[i])
    wbk.save(str(lujing) + ".xlsx")
    msg.showinfo("保存成功", "数据已经保存")


menuopen.add_command(label="载入数据", command=openfile)  # 调用函数
menuopenxl.add_command(label="打开xlsx", command=openxlsx)  # 调用函数
menuopenxl.add_command(label="保存xlsx", command=savexlsx)  # 调用函数
root.config(menu=menubar)  # 配置菜单 不用说了


def start():  # 核心代码
    xlsxyn.clear()
    xlsxyn.insert(0, "校验结果")
    right.delete("1.0", "end")  # 载入清空文本框2
    idtext2 = idtext.get("0.0", "end")  # 获取文本框1
    idtext3 = idtext2.splitlines()  # 分割文本框、
    idm = idtext3  # 变了载入分割的数据
    for i in range(len(idm)):  # 循环匹配身份证
        id = idm[i]  # 变量置入
        if (len(id) < 17):  # 小于18位不是真正的身份证
            right.insert(0.1, idm[i] + " 信息错误!\n")
        else:
            jyma = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 验证身份证关键的key
            idsx = []  # 置入身份证数据
            add = []
            pp = ""
            number = 0
            for i in range(17):  # 循环十七次表示18位身份证
                idsx.insert(i, id[i])  # 加入ID数据
                pp += idsx[i]  # 转换成文本 方便以后相加于最后一位数
                a = int(idsx[i])  # 身份证的数据
                b = int(jyma[i])  # 身份证验证的key
                add.append(a * b)  # 相乘到add变量
                number += int(add[i])  # 相加相加

            know = number % 11  # 取摸
            key = {0: "1", 1: "0", 2: "X", 3: "9", 4: "8", 5: "7", 6: "6", 7: "5", 8: "4", 9: "3",
                   10: "2"}  # 字典为匹配身份证最后一位
            man = list(key.keys())  # man 列出键值
            woman = list(key.values())  # woman 列出数值
            for i in range(11):  # 循环11次位数值的匹配
                if know == man[i]:  # 匹配指定的数字到键值后等成于数值
                    yep = pp + woman[i]  # 身份证整数字
                    if (yep == id):  # 被处理的身份证数字如果等于载入的数字
                        right.insert("end", id + " 通过国家身份数据库!\n")  # 则正确
                        xlsxyn.append("正确")
                    else:
                        right.insert("end", id + " 身份信息错误!\n")  # 则错误
                        xlsxyn.append("错误")


idtext = tkinter.Text(root, height="10")
idtext.pack()

tkinter.Button(root, text="开始校验", font=(30), command=start).place(x=155, y=142)
right = tkinter.Text(root, height="20")
right.place(y=180)
tkinter.Label(root, text="姓名列:").place(x=12, y=450)
namekeytext = tkinter.Entry(root, width=5)
namekeytext.place(x=60, y=450)
tkinter.Label(root, text="证号列:").place(x=100, y=450)
idkeytext = tkinter.Entry(root, width=5)
idkeytext.place(x=150, y=450)


def set():
    global namekey
    global idkey
    if namekeytext.get() == "":
        msg.showinfo("提示", "请输入名列:")
    elif idkeytext.get() == "":
        msg.showinfo("提示", "请输入证号列:")
    else:
        namekey = int(namekeytext.get())
        idkey = int(idkeytext.get())


tkinter.Label(root, text="一八微机一班 2019 年 4 月 1 日开发", fg="black").place(x=190, y=450)
root.mainloop()
