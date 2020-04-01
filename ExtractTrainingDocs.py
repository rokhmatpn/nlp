import pymssql
import os

conn = pymssql.connect("10.11.22.100", "sa", "sqlbi4dm!n", "TARKDW")
cursor = conn.cursor()
cursor.execute("select distinct(category) from gn4categories")

parentfolder = "c:/KompasTrainingDoc2016"

# get parent categories 
categories = []
for row in cursor:
	dirCat = row[0].encode("utf-8")
	categories.append(dirCat)
	
for cat in categories:
	print(cat)
	if not os.path.exists(cat):
		os.makedirs(cat)
	
	#get files for each category
	curStories = conn.cursor()
	curStories.execute("""
		select top 500 a.id, a.title, a.category, c.category, a.body 
		from dumpforpostagger a 
			join GN4Categories c on (a.category=c.subcategory) where c.category = '%s'""" % cat)
	i = 1
	for rowStories in curStories:
		filename = "%s/%s/%s.txt" % (parentfolder, cat, rowStories[0])
		print("creating story number:%s id:%s" % (i, filename))
		newfile = open(filename, "w")
		newfile.write(rowStories[4].encode("utf-8"))
		newfile.close();
		i += 1
	break

conn.close()