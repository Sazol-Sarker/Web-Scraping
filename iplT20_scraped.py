#web scraping using bs4
import requests 
import pandas as pd
from bs4 import BeautifulSoup
import html5lib
import lxml
url="https://www.iplt20.com/auction"


r= requests.get(url)
print(r)#if r=200 yes , r=403 denied

soup=BeautifulSoup(r.text,"lxml")

table=soup.find("table",class_="ih-td-tab auction-tbl")

#auction table extracted
print(table)







