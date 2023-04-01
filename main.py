#web scraping using bs4
import requests 
from bs4 import BeautifulSoup
url="https://codewithharry.com"


r= requests.get(url)

htmlContent=r.content
# print(htmlContent)

soup=BeautifulSoup(htmlContent,'html.parser')
# print(soup.prettify)

# get title of html page 
title=soup.title 
# print(title)
# print(type(title))

#find 1st para
para=soup.find('p')
para_cls=soup.find('p')['class'] # get all classes of 1st paragraph
# print(para)
# print(para_cls)
# get all paragraphs 
paras=soup.find_all('p')
# print(paras)

#get all anchor tags
anchors=soup.find_all('a')
# print(anchors)

#get texts from tags
# print(soup.find('p').get_text())
# print(soup.get_text())
all_links=set()

# GET ALL LINKS FROM A WEBSITE ANCHOR TAGS 
for links in anchors:
    if links!='#': 
         link="https://codewithharry.com"+links.get('href')
         all_links.add (link)  
        #  print(link)
# print(all_links)

#get all content of para from html
html_comment="<p>A paragraph</p>"

soup_comment=BeautifulSoup(html_comment)
#content of paragraph
# print(soup_comment.p)
# # bs4.element.tag
# print(type(soup_comment.p)) 


#extracting content of a target div using its id



url1="https://www.codewithharry.com/login/"


r1= requests.get(url1)

htmlContent1=r1.content
# print(htmlContent)

soup3=BeautifulSoup(htmlContent1,'html.parser')
# print(soup3)

imgpreview2=soup3.find(id="imgpreview2")
# print(imgpreview2) # got the div
# print(imgpreview2.contents) # got the div content source

# for i in imgpreview2:
#      print (i)# iterste childs



#access login modal in soup
mod=soup3.select('.Toastify')
print(mod)




