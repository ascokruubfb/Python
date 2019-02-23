from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.17k.com/chapter/2920605/36467658.html").read().decode("utf-8")
soup = BeautifulSoup(html,'html.parser')
text=soup.find_all('div',{"class":"p"})
for i in text:
    print(i.get_text())
    x=open("小说.txt","w")
    x.write("本小说由爬虫程序生成。。。")
    x.write(i.get_text())
