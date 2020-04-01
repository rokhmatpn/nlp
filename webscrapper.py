## For downloading HTML structure
import requests
## For Scraping through HTML
from bs4 import BeautifulSoup
## For visualising data in a table
import pandas as pd
 
## Mentioning the target url
targetUrl = 'https://dimensionless.in/blog'
## Downloading the HTML content from the target page
r= requests.get(targetUrl)
data=r.text
##Converting the data into a Beautiful Soup compatible object
soup=BeautifulSoup(data, 'lxml')
 
## Lists for holding the values
blog_names=[]
author_names=[]
blog_dates=[]
 
## Iterating through all the articles and extracting blog title, author name and blog date
for listing in soup.find_all('article'):
    for blog_name in listing.find('h2', attrs={'class':"entry-title"}):
        blog_names.append(blog_name.text)
    for author_name in listing.find('span', attrs={'class':"author vcard"}):
        author_names.append(author_name.text)
    for blog_date in listing.find('span', attrs={'class':"published"}):
        blog_dates.append(blog_date)
        
blogData=pd.DataFrame({"Blog Name":blog_names, "Author Name":author_names, "Blog Dates":blog_dates})

print blogData