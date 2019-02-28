#! /usr/bin/python

import smtplib
import os
import json
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# me == my email address
# you == recipient's email address
me = 'johnoldmanworkspace@gmail.com'
you = ['nguyenvietbac96@gmail.com', 'dinh.tuanminh@vietanalytics.vn', 'dungnd560@gmail.com', 'tdhoang2103@gmail.com', 'nguyenthuylien203@gmail.com']

# you = 'nguyenvietbac96@gmail.com'
# you = 'nguyenvietbac96@gmail.com'
#######################################
file_data = []
#####################################
# 1
file_temp = []
if os.path.exists("moit.json") and os.path.getsize("moit.json") > 0:
	with open('moit.json', encoding="utf-8") as f:
		file_moit = json.load(f)
	if os.path.exists("old_moit.json") and os.path.getsize("old_moit.json") > 0:	
		with open('old_moit.json', encoding="utf-8") as f:
			file_old_moit = json.load(f)
		for x in file_moit:
			if x not in file_old_moit:
				file_temp.append(x)
	else:
		file_temp = list(file_moit)
temp = list(file_temp)
file_temp = [dict(t) for t in {tuple(d.items()) for d in temp}]
file_data.extend(file_temp)
#############################################
# 2
file_temp = []
if os.path.exists("mpi.json") and os.path.getsize("mpi.json") > 0:
	with open('mpi.json', encoding="utf-8") as f:
		file_mpi = json.load(f)
	if os.path.exists("old_mpi.json") and os.path.getsize("old_mpi.json") > 0:	
		with open('old_mpi.json', encoding="utf-8") as f:
			file_old_mpi = json.load(f)
		for x in file_mpi:
			if x not in file_old_mpi:
				file_temp.append(x)
	else:
		file_temp = list(file_mpi)
temp = list(file_temp)
file_temp = [dict(t) for t in {tuple(d.items()) for d in temp}]
file_data.extend(file_temp)
###############################################
# 3
file_temp = []
if os.path.exists("mof.json") and os.path.getsize("mof.json") > 0:
	with open('mof.json', encoding="utf-8") as f:
		file_mof = json.load(f)
	if os.path.exists("old_mof.json") and os.path.getsize("old_mof.json") > 0:	
		with open('old_mof.json', encoding="utf-8") as f:
			file_old_mof = json.load(f)
		for x in file_mof:
			if x not in file_old_mof:
				file_temp.append(x)
	else:
		file_temp = list(file_mof)
temp = list(file_temp)
file_temp = [dict(t) for t in {tuple(d.items()) for d in temp}]
file_data.extend(file_temp)

###################################################
# 4
file_temp = []
if os.path.exists("sbv.json") and os.path.getsize("sbv.json") > 0:
	with open('sbv.json', encoding="utf-8") as f:
		file_sbv = json.load(f)
	if os.path.exists("old_sbv.json") and os.path.getsize("old_sbv.json") > 0:	
		with open('old_sbv.json', encoding="utf-8") as f:
			file_old_sbv = json.load(f)
		for x in file_sbv:
			if x not in file_old_sbv:
				file_temp.append(x)
	else:
		file_temp = list(file_sbv)
# temp = list(file_temp)
# file_temp = [dict(t) for t in {tuple(d.items()) for d in temp}]
temp = []
for x in file_temp:
	if x not in temp:
		temp.append(x)
file_temp = list(temp)

file_data.extend(file_temp)
##################################################
# 5
file_temp = []
if os.path.exists("vcb.json") and os.path.getsize("vcb.json") > 0:
	with open('vcb.json', encoding="utf-8") as f:
		file_vcb = json.load(f)
	if os.path.exists("old_vcb.json") and os.path.getsize("old_vcb.json") > 0:	
		with open('old_vcb.json', encoding="utf-8") as f:
			file_old_vcb = json.load(f)
		for x in file_vcb:
			if x not in file_old_vcb:
				file_temp.append(x)
	else:
		file_temp = list(file_vcb)
# temp = list(file_temp)
# file_temp = [dict(t) for t in {tuple(d.items()) for d in temp}]
temp = []
for x in file_temp:
	if x not in temp:
		temp.append(x)
file_temp = list(temp)
file_data.extend(file_temp)

####################################################
# 6
file_temp = []
if os.path.exists("vib.json") and os.path.getsize("vib.json") > 0:
	with open('vib.json', encoding="utf-8") as f:
		file_vib = json.load(f)
	if os.path.exists("old_vib.json") and os.path.getsize("old_vib.json") > 0:	
		with open('old_vib.json', encoding="utf-8") as f:
			file_old_vib = json.load(f)
		for x in file_vib:
			if x not in file_old_vib:
				file_temp.append(x)
	else:
		file_temp = list(file_vib)
temp = list(file_temp)
file_temp = [dict(t) for t in {tuple(d.items()) for d in temp}]
file_data.extend(file_temp)

#########################################################
# 7
file_temp = []
con = 0
if os.path.exists("vne.json") and os.path.getsize("vne.json") > 0:
	with open('vne.json', encoding="utf-8") as f:
		file_vne = json.load(f)
		# clear duplicated items
		# temp = []
		# dup = 0
		# for x in range(len(file_vne)):
		# 	for y in range(len(file_vne)):
		# 		if x!=y and file_vne[x]["title"] == file_vne[y]["title"]:
		# 			dup = 1
		# 			break
		# 	if dup == 1:
		# 		continue
		# 	else:
		# 		temp.append(file_vne[x])
		# 	dup = 0
		# file_vne = list(temp)

	if os.path.exists("old_vne.json") and os.path.getsize("old_vne.json") > 0:	
		with open('old_vne.json', encoding="utf-8") as f:
			file_old_vne = json.load(f)
		# check = 1
		for x in range(len(file_vne)):
			check = 1
			if file_vne[x] in file_old_vne:
				continue
			for y in range(len(file_temp)):
				if file_vne[x]['title'] == file_temp[y]['title']:
					check = 0
					break
			if check == 1:
				file_temp.append(file_vne[x])
	else:
		file_temp = list(file_vne)

for x in range(len(file_temp)):
	temp = file_temp[x]['title'][0].split()
	for y in range(0,len(temp)-1):
		if (temp[y] == "thế" or temp[y] == "Thế") and temp[y+1] == "giới":
			file_temp[x]['title'][0] = "* " + file_temp[x]['title'][0]
		if temp[y] == "Mỹ":
			file_temp[x]['title'][0] = "* " + file_temp[x]['title'][0]
		if (temp[y] == "tăng" or temp[y] == "Tăng") and temp[y+1] == "trưởng":
			file_temp[x]['title'][0] = "* " + file_temp[x]['title'][0]
		if (temp[y] == "chất" or temp[y] == "Chất") and temp[y+1] == "lượng":
			file_temp[x]['title'][0] = "* " + file_temp[x]['title'][0]

for x in range(len(file_temp)):
	file_temp[x]["link"] = file_temp[x]["link"][0]
	if file_temp[x]["description"] != []:
		file_temp[x]["description"] = file_temp[x]["description"][0]
	else:
		file_temp[x]["description"] = ""
	file_temp[x]["date"] = file_temp[x]["date"][0]
	file_temp[x]["title"] = file_temp[x]["title"][0]
temp = list(file_temp)
file_temp = [dict(t) for t in {tuple(d.items()) for d in temp}]
file_data.extend(file_temp)
################################################
# 8
# chi gui "the gioi", "kinh doanh", "bat dong san"
file_temp = []
if os.path.exists("dantri.json") and os.path.getsize("dantri.json") > 0:
	with open('dantri.json', encoding="utf-8") as f:
		file_dantri = json.load(f)

	if os.path.exists("old_dantri.json") and os.path.getsize("old_dantri.json") > 0:	
		with open('old_dantri.json', encoding="utf-8") as f:
			file_old_dantri = json.load(f)
		for x in range(len(file_dantri)):
			check = 1
			if file_dantri[x] in file_old_dantri:
				continue
			# if file_dantri[x]["tab"] == "the gioi" or file_dantri[x]["tab"] == "kinh doanh" or file_dantri[x]["tab"] == "bat dong san":
				# continue
			if file_dantri[x]["tab"] == "kinh doanh":	
				for y in range(len(file_temp)):
					if file_dantri[x]['title'] == file_temp[y]['title']:
						check = 0
						break
				if check == 1:
					file_temp.append(file_dantri[x])

	else:
		file_temp = list(file_dantri)

for x in range(len(file_temp)):
	temp = file_temp[x]['title'][0].split()
	for y in range(0,len(temp)-1):
		if (temp[y] == "thế" or temp[y] == "Thế") and temp[y+1] == "giới":
			file_temp[x]['title'][0] = "* " + file_temp[x]['title'][0]
		if temp[y] == "Mỹ":
			file_temp[x]['title'][0] = "* " + file_temp[x]['title'][0]
		if (temp[y] == "tăng" or temp[y] == "Tăng") and temp[y+1] == "trưởng":
			file_temp[x]['title'][0] = "* " + file_temp[x]['title'][0]
		if (temp[y] == "chất" or temp[y] == "Chất") and temp[y+1] == "lượng":
			file_temp[x]['title'][0] = "* " + file_temp[x]['title'][0]

for x in range(len(file_temp)):
	file_temp[x]["link"] = file_temp[x]["link"][0]
	if file_temp[x]["description"] != []:
		file_temp[x]["description"] = file_temp[x]["description"][0]
	else:
		file_temp[x]["description"] = ""
	file_temp[x]["date"] = file_temp[x]["date"][0]
	file_temp[x]["title"] = file_temp[x]["title"][0]
temp = list(file_temp)
file_temp = [dict(t) for t in {tuple(d.items()) for d in temp}]

file_data.extend(file_temp)

################################################
# 9
# chi gui "business", "Company news", "enviroment" , "money", "politics" , "science", "technology", "top news", "US news", "World"
file_temp = []
if os.path.exists("reuters.json") and os.path.getsize("reuters.json") > 0:
	with open('reuters.json', encoding="utf-8") as f:
		file_reuters = json.load(f)

	if os.path.exists("old_reuters.json") and os.path.getsize("old_reuters.json") > 0:	
		with open('old_reuters.json', encoding="utf-8") as f:
			file_old_reuters = json.load(f)

		for x in range(len(file_reuters)):
			check = 1
			if file_reuters[x] in file_old_reuters:
				continue
			# if file_reuters[x]["tab"] == "reuters/businessNews" or file_reuters[x]["tab"] == "reuters/companyNews" or file_reuters[x]["tab"] == "reuters/environment" or file_reuters[x]["tab"] == "news/wealth" or file_reuters[x]["tab"] == "Reuters/PoliticsNews" or file_reuters[x]["tab"] == "reuters/scienceNews" or file_reuters[x]["tab"] == "reuters/technologyNews" or file_reuters[x]["tab"] == "reuters/topNews" or file_reuters[x]["tab"] == "Reuters/worldNews" or file_reuters[x]["tab"] == "Reuters/domesticNews":
			if file_reuters[x]["tab"] == "reuters/businessNews" or file_reuters[x]["tab"] == "reuters/companyNews":
				for y in range(len(file_temp)):
					if file_reuters[x]['title'] == file_temp[y]['title']:
						check = 0
						break
				if check == 1:
					file_temp.append(file_reuters[x])

	else:
		file_temp = list(file_reuters)

for x in range(len(file_temp)):
	temp = file_temp[x]['title'][0].split()
	for y in range(0,len(temp)-1):
		if (temp[y] == "Brexit"):
			file_temp[x]['title'][0] = "* " + file_temp[x]['title'][0]
		if temp[y] == "reports" or temp[y] == "Reports":
			file_temp[x]['title'][0] = "* " + file_temp[x]['title'][0]
		# if (temp[y] == "tăng" or temp[y] == "Tăng") and temp[y+1] == "trưởng":
		# 	file_temp[x]['title'][0] = "* " + file_temp[x]['title'][0]
		# if (temp[y] == "chất" or temp[y] == "Chất") and temp[y+1] == "lượng":
		# 	file_temp[x]['title'][0] = "* " + file_temp[x]['title'][0]

for x in range(len(file_temp)):
	file_temp[x]["link"] = file_temp[x]["link"][0]
	if file_temp[x]["description"] != []:
		file_temp[x]["description"] = file_temp[x]["description"][0]
	else:
		file_temp[x]["description"] = ""
	file_temp[x]["date"] = file_temp[x]["date"][0]
	file_temp[x]["title"] = file_temp[x]["title"][0]
temp = list(file_temp)
file_temp = [dict(t) for t in {tuple(d.items()) for d in temp}]

file_data.extend(file_temp)

################################################
# 10 The Economist
# chi gui "the-world-this-week", "leaders", "special-report", "international", "business", "finance-and-economics", "economic-and-financial-indicators" 
file_temp = []
if os.path.exists("economist.json") and os.path.getsize("economist.json") > 0:
	with open('economist.json', encoding="utf-8") as f:
		file_economist = json.load(f)

	if os.path.exists("old_economist.json") and os.path.getsize("old_economist.json") > 0:	
		with open('old_economist.json', encoding="utf-8") as f:
			file_old_economist = json.load(f)

		for x in range(len(file_economist)):
			check = 1
			if file_economist[x] in file_old_economist:
				continue
			if file_economist[x]["tab"] == "the-world-this-week" or file_economist[x]["tab"] == "leaders" or file_economist[x]["tab"] == "special-report" or file_economist[x]["tab"] == "international" or file_economist[x]["tab"] == "business" or file_economist[x]["tab"] == "finance-and-economics" or file_economist[x]["tab"] == "economic-and-financial-indicators":
				# continue
				for y in range(len(file_temp)):
					if file_economist[x]['title'] == file_temp[y]['title']:
						check = 0
						break
				if check == 1:
					file_temp.append(file_economist[x])

	else:
		file_temp = list(file_economist)

for x in range(len(file_temp)):
	temp = file_temp[x]['title'][0].split()
	for y in range(0,len(temp)-1):
		if (temp[y] == "Brexit"):
			file_temp[x]['title'][0] = "* " + file_temp[x]['title'][0]
		if temp[y] == "reports" or temp[y] == "Reports":
			file_temp[x]['title'][0] = "* " + file_temp[x]['title'][0]
		if (temp[y] == "money"):
			file_temp[x]['title'][0] = "* " + file_temp[x]['title'][0]
		# if (temp[y] == "chất" or temp[y] == "Chất") and temp[y+1] == "lượng":
		# 	file_temp[x]['title'][0] = "* " + file_temp[x]['title'][0]

for x in range(len(file_temp)):
	file_temp[x]["link"] = file_temp[x]["link"][0]
	if file_temp[x]["description"] != []:
		file_temp[x]["description"] = file_temp[x]["description"][0]
	else:
		file_temp[x]["description"] = ""
	file_temp[x]["date"] = file_temp[x]["date"][0]
	file_temp[x]["title"] = file_temp[x]["title"][0]
temp = list(file_temp)
file_temp = [dict(t) for t in {tuple(d.items()) for d in temp}]

file_data.extend(file_temp)

################################################
# 11 IMF

file_temp = []
if os.path.exists("imf.json") and os.path.getsize("imf.json") > 0:
	with open('imf.json', encoding="utf-8") as f:
		file_imf = json.load(f)
		# print(file_imf)
	if os.path.exists("old_imf.json") and os.path.getsize("old_imf.json") > 0:	
		with open('old_imf.json', encoding="utf-8") as f:
			file_old_imf = json.load(f)

		for x in range(len(file_imf)):
			check = 1
			if file_imf[x] in file_old_imf:
				continue
			if True:
				# continue
				for y in range(len(file_temp)):
					if file_imf[x]['title'] == file_temp[y]['title']:
						check = 0
						break
				if check == 1:
					file_temp.append(file_imf[x])

	else:
		file_temp = list(file_imf)

for x in range(len(file_temp)):
	temp = file_temp[x]['title'][0].split()
	for y in range(0,len(temp)-1):
		if (temp[y] == "Brexit"):
			file_temp[x]['title'][0] = "* " + file_temp[x]['title'][0]
		if temp[y] == "reports" or temp[y] == "Reports":
			file_temp[x]['title'][0] = "* " + file_temp[x]['title'][0]
		if (temp[y] == "money"):
			file_temp[x]['title'][0] = "* " + file_temp[x]['title'][0]
		# if (temp[y] == "chất" or temp[y] == "Chất") and temp[y+1] == "lượng":
		# 	file_temp[x]['title'][0] = "* " + file_temp[x]['title'][0]

for x in range(len(file_temp)):
	file_temp[x]["link"] = file_temp[x]["link"][0]
	if file_temp[x]["description"] != []:
		file_temp[x]["description"] = file_temp[x]["description"][0]
	else:
		file_temp[x]["description"] = ""
	file_temp[x]["date"] = file_temp[x]["date"][0]
	file_temp[x]["title"] = file_temp[x]["title"][0]
temp = list(file_temp)
file_temp = [dict(t) for t in {tuple(d.items()) for d in temp}]

file_data.extend(file_temp)

################################################
# 12 FED

file_temp = []
if os.path.exists("fed.json") and os.path.getsize("fed.json") > 0:
	with open('fed.json', encoding="utf-8") as f:
		file_fed = json.load(f)
		# print(file_fed)
	if os.path.exists("old_fed.json") and os.path.getsize("old_fed.json") > 0:	
		with open('old_fed.json', encoding="utf-8") as f:
			file_old_fed = json.load(f)

		for x in range(len(file_fed)):
			check = 1
			if file_fed[x] in file_old_fed:
				continue
			if True:
				# continue
				for y in range(len(file_temp)):
					if file_fed[x]['title'] == file_temp[y]['title']:
						check = 0
						break
				if check == 1:
					file_temp.append(file_fed[x])

	else:
		file_temp = list(file_fed)

for x in range(len(file_temp)):
	temp = file_temp[x]['title'][0].split()
	for y in range(0,len(temp)-1):
		if (temp[y] == "Brexit"):
			file_temp[x]['title'][0] = "* " + file_temp[x]['title'][0]
		if temp[y] == "reports" or temp[y] == "Reports":
			file_temp[x]['title'][0] = "* " + file_temp[x]['title'][0]
		if (temp[y] == "money"):
			file_temp[x]['title'][0] = "* " + file_temp[x]['title'][0]
		# if (temp[y] == "chất" or temp[y] == "Chất") and temp[y+1] == "lượng":
		# 	file_temp[x]['title'][0] = "* " + file_temp[x]['title'][0]

for x in range(len(file_temp)):
	file_temp[x]["link"] = file_temp[x]["link"][0]
	if file_temp[x]["description"] != []:
		file_temp[x]["description"] = file_temp[x]["description"][0]
	else:
		file_temp[x]["description"] = ""
	file_temp[x]["date"] = file_temp[x]["date"][0]
	file_temp[x]["title"] = file_temp[x]["title"][0]
temp = list(file_temp)
file_temp = [dict(t) for t in {tuple(d.items()) for d in temp}]

file_data.extend(file_temp)

################################################

if file_data == []:
	html = """\
<html>
  <head></head>
  <body>
  		<p><big> KHÔNG CÓ TIN MỚI </big></p>
"""
	html = html +   """</body>
</html>
"""	
else :
	html = """\
<html>
  <head></head>
  <body>
"""
for x in range(len(file_data)):
	html = html + """<p>
""" + "<a href=\"" + file_data[x]["link"] + "\">" + file_data[x]["title"] + "</a> " + file_data[x]["source"] + " (" + file_data[x]["date"] + ")" + """
</p>
"""
	html = html +   """</body>
</html>
"""

# 	msg = msg + file_data[x]["link"] + " VIB bank " + file_data[x]["date"] + """
# """ + file_data[x]["link"] + """
# """

# with open("update_news.json", "w") as f:
# 	json.dump(file_data, f, indent=4)

#######################################

# Create message container - the correct MIME type is multipart/alternative.
date = datetime.datetime.now()
date = str(date)
# print("NEWs " + date[0:13] + "-h")
msg = MIMEMultipart('alternative')
msg['Subject'] = "NEWs " + date[0:13] + "-h"
msg['From'] = me
msg['To'] = ", ".join(you)
# msg['To'] = you

# Create the body of the message (a plain-text and an HTML version).
# text = "Hi!\nHow are you?\nHere lallsalfsda is the link you wanted:\nhttp://www.python.org"
# html = """\
# <html>
#   <head></head>
#   <body>
#     <p>Hi!<br>
#        How are you?<br>
#        Here is the <a href="http://www.python.org">link</a> you wanted.
#     </p>
#   </body>
# </html>
# """

# Record the MIME types of both parts - text/plain and text/html.
# part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
# msg.attach(part1)
msg.attach(part2)

username = 'johnoldmanworkspace@gmail.com'
password = '112358pi'

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(me, you, msg.as_string())
server.quit()

print("Done")
# # Send the message via local SMTP server.
# s = smtplib.SMTP('localhost')
# # sendmail function takes 3 arguments: sender's address, recipient's address
# # and message to send - here it is sent as one string.
# s.sendmail(me, you, msg.as_string())
# s.quit()