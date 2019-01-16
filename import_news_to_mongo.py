# -*- coding: utf-8 -*-
import os
import json
import pymongo
import datetime

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["News"]
names = mydb.collection_names()

date = datetime.datetime.now().date()
date = str(date)

mycol = mydb["News_"+ date]

if os.path.exists("update_news.json") and os.path.getsize("update_news.json") > 0:	
	with open('update_news.json', encoding="utf-8") as f:
		file_update_news = json.load(f)
	mycol.insert(file_update_news)

myclient.close()
