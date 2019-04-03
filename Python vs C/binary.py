binary=input("enter your number:")
ejz=[]
yea=binary
while True:
    yea=int(yea)/2
    split=str(yea)
    if split[-1] == "0":
        ejz.insert(0,"0")
    elif split[-1] == "5":
        ejz.insert(0,"1")
    if yea==0.5:
        break
    elif yea==1.0:
        break
ejzx=""
for i in range(len(ejz)):
    ejzx+=ejz[i]
print("success:"+ejzx)
