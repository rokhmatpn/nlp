# CREATE HTTP REQUEST #

import requests

url = "http://10.9.8.237:9200"

# LOAD DATA #

import pymssql
import os

conn = pymssql.connect("10.11.22.100", "sa", "sqlbi4dm!n", "TARKDW")
cursor = conn.cursor()
cursor.execute("select distinct(category) from gn4categories")


# get parent categories 
categories = []
for row in cursor:
	dirCat = row[0].encode("utf-8", 'replace').decode()
	categories.append(dirCat)

for cat in categories:
	print(cat)
	
	#get files for each category
	curStories = conn.cursor()
	curStories.execute("""
		select top 200 a.id, a.title, a.category, c.category, a.body 
		from dumpforpostagger a 
			join GN4Categories c on (a.category=c.subcategory) where c.category = '%s'""" % cat)
	i = 1
	for rowStories in curStories:
		data = '''{
"category":"%s",
"content":"%s"
}''' % (cat, rowStories[4].encode("ascii", 'replace').decode().replace("?","").replace("\n"," ").replace("\r"," ").replace("\t"," ").replace("\"",""));

		docid = rowStories[0];

		print("%s. ID:%s \n %s" % (i, docid, data));
		print("%s/trainingset/document/%s" % (url, docid))

		response = requests.post("%s/trainingset/document/%s" % (url, docid), data=data, headers={"Content-Type": "application/json"})
		print(response)
		print(response.text)

		i += 1		
#	break

conn.close()

