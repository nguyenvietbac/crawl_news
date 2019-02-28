# -*- coding: utf-8 -*-
import pypyodbc
import pyodbc
import json
import pymongo
import os
#####################################################
# print("new data found, creating new access file")

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Administrator\Documents\share_folder\news1\temp.accdb;')
cursor = conn.cursor()
cursor2 = conn.cursor()
for table in cursor.tables():
	if table.table_type == "TABLE":
		drop = "DROP TABLE [{0}]".format(table.table_name)
		print drop
		cursor2.execute(drop)
conn.commit()
conn.close()

#####################################################
dbname = r'C:\Users\Administrator\Documents\share_folder\news1\temp.accdb'     
constr = "DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={0};".format(dbname)

dbconn = pypyodbc.connect(constr)
cur = dbconn.cursor()

cur.execute("""CREATE TABLE data (
				 ID autoincrement,
				 title varchar(100),
				 link varchar(50),
				 source varchar(50),
				 "date" varchar(50),
				 description varchar(100),
				 tab varchar(50));""")
dbconn.commit()
dbconn.close()

# ####################################################

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Administrator\Documents\share_folder\news1\temp.accdb;')
cursor = conn.cursor()

if os.path.exists("ce.json") and os.path.getsize("ce.json") > 0:	
	with open('ce.json') as f:
		file_data = json.load(f)
for x in file_data:
	# print(type(x["tab"]))
	if type(x["tab"]) is list:
		x["tab"] = x["tab"][0]
	na = [x["title"], x["link"], x["source"], x["date"], "", x["tab"]]
	ind_data = ('''
					INSERT INTO data (title, link, source, "date", description, tab)
					VALUES(?, ?, ?, ?, ?, ?)

			   ''')

	cursor.execute(ind_data, na)

conn.commit()
conn.close()
