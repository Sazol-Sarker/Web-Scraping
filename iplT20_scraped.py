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
# print(table)

#extracted table header
header=table.find_all("th")
# print(header)

hTitle=[]

for i in header:
    title=i.text 
    hTitle.append(title)

# print(hTit le)

df=pd.DataFrame(columns=hTitle)
# print(df)
ind =0
rows=table.find_all("tr")
for i in rows[1:]:
    data=i.find_all("td")
    # print(data)
    row=[tr.text for tr in data]
    df.loc[ind]=row
    ind+=1
    # print(row)

print(df)
df.to_csv("IPL_auction.csv")

