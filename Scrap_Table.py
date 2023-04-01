#web scraping using bs4
import requests 
import pandas as pd
from bs4 import BeautifulSoup
import html5lib
import lxml
url="https://www.scrapethissite.com/pages/forms/"


r= requests.get(url)
# print(r)#if r=200 yes , r=403 denied

#this is html content
htmlContent=r.content
# print(htmlContent)

soup=BeautifulSoup(htmlContent,'html.parser')
# print(soup.prettify)#preety html fetched


soup1=BeautifulSoup(r.text,"lxml")

FullTable=soup1.find("table",class_="table")

# print(FullTable)#full table fetched

#table header fetch
headerList=FullTable.find_all("th")
# print(headerList) # all header tag with contents

#all header titles iterated
for i in headerList:
        x=i.text 
        print(x)
        
        









