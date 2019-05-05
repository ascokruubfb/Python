import urllib.request as e
print("Welcome to website scan script to me say:\n"
      "Hello Wolrd@@@@@@@@@@@@@@@@@@@@@@")
file=open("url.txt")
admin=file.readlines()
website=""
sucfile=""
def start():
    global website,sucfile
    url=input("Scan url:")
    if url=="":
        start()
    else:
        website=url
        saf=input("please save success file:")
        sucfile=saf
        print("Just loading,waiting......")
start()
for i in range(len(admin)):
    try:
        e.urlopen(website+admin[i])
        out="Success >>> "+website+admin[i]
        print(out[0:-1])
        f=open(sucfile,"a")
        f.write(out)
    except:
        print("Error NOT FOUND")
