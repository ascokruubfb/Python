from flask import Flask,render_template,request
app=Flask(__name__)
msg=[]
@app.route("/",methods=['get'])
def login():
    return render_template("index.html",msg=msg)
@app.route("/send.asp",methods=['GET','POST'])
def send():
    global namex
    valu=request.args
    x=list(valu.values())
    msg.append(x[0])
    return "写入成功"

if __name__=="__main__":
    app.run(host="192.168.1.6",debug=True)
