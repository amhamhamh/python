#!C:\Users\amham\AppData\Local\Programs\Python\Python38-32\python.exe
#!python
from bs4 import BeautifulSoup
from urllib.request import urlopen

response = urlopen('https://www.daum.net/')
soup = BeautifulSoup(response, 'html.parser')
i=0
for anchor in soup.select("a.link_favorsch"):
    i+=1
    print(str(i)+'위'+anchor.get_text())
