from urllib.request import urlopen
import re
data=urlopen("http://www.17k.com/list/2920605.html").read().decode("utf-8")
book=re.findall("/chapter/2920605/.*html",data)
for i in range(len(book)):
    url="http://www.17k.com/"+book[i]
    data=urlopen(url).read().decode("utf-8")
    title=re.findall("<title>.*</title>",data)
    titlereal=title[0]
    thisisname=titlereal[7:-17]
    a=re.findall(".*<br /><br />",data)
    b=re.findall("[^<br /><br />&#12288;&#12288;][^<b]*",a[0])
    a=""
    for i1 in range(len(b)):
        a+=b[i1]
    print(str(i+1)+" OK!")
    x=open(thisisname+".txt","w")
    x.write(a)
