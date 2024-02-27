import requests
from bs4 import BeautifulSoup



url="https://www.ebanglalibrary.com/33372/%e0%a7%a6%e0%a7%a6%e0%a7%a7-%e0%a6%85%e0%a6%a8%e0%a7%81%e0%a6%95%e0%a7%8d%e0%a6%b0%e0%a6%ae%e0%a6%a3%e0%a6%bf%e0%a6%95%e0%a6%be%e0%a6%a7%e0%a7%8d%e0%a6%af%e0%a6%be%e0%a7%9f-%e0%a6%a8%e0%a7%88/"
response=requests.get(url)
html_content=response.content

soup=BeautifulSoup(html_content,"html.parser")
#title=soup.find("")
title=soup.find_all("h1", {"class": "page-header-title"})
divs1 = soup.find("div", {"class": "entry-content entry-content-single"}).find("p")


for i in divs1:
    print(i)


