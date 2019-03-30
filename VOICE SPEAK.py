import tkinter
import pyttsx3
engin=pyttsx3.init()
rate=engin.getProperty("rate")
engin.setProperty("rate",rate-40)
engin.say("a ")
engin.runAndWait()
window=tkinter.Tk()
window.title("语音朗读软件")
window.geometry("400x400")
textx=tkinter.Text(window,height=9,width=60,font=("微软雅黑",20))
textx.pack()
def speak():
    engin.say(textx.get(1.0,"end"))
    engin.runAndWait()
tkinter.Button(window,text="开始朗读",font=(10),height=30,width=20,command=speak).pack()
window.mainloop()
