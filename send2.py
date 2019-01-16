#! /usr/bin/python

import smtplib
import os
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# me == my email address
# you == recipient's email address
me = 'johnoldmanworkspace@gmail.com'
you = 'nguyenvietbac96@gmail.com'
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
file_data.extend(file_temp)

#########################################################
# 7
file_temp = []
con = 0
if os.path.exists("vne.json") and os.path.getsize("vne.json") > 0:
	with open('vne.json', encoding="utf-8") as f:
		file_vne = json.load(f)
		# clear duplicated items
		temp = []
		dup = 0
		for x in range(len(file_vne)):
			for y in range(len(file_vne)):
				if x!=y and file_vne[x]["title"] == file_vne[y]["title"]:
					dup = 1
					break
			if dup == 1:
				continue
			else:
				temp.append(file_vne[x])
			dup = 0
		file_vne = list(temp)

	if os.path.exists("old_vne.json") and os.path.getsize("old_vne.json") > 0:	
		with open('old_vne.json', encoding="utf-8") as f:
			file_old_vne = json.load(f)
		for x in file_vne:
			if x not in file_old_vne:
				file_temp.append(x)
	else:
		file_temp = list(file_vne)
for x in range(len(file_temp)):
	file_temp[x]["link"] = file_temp[x]["link"][0]
	file_temp[x]["description"] = file_temp[x]["description"][0]
	file_temp[x]["date"] = file_temp[x]["date"][0]
	file_temp[x]["title"] = file_temp[x]["title"][0]
file_data.extend(file_temp)
################################################
# 8
# chi gui "the gioi", "kinh doanh", "bat dong san"
file_temp = []
if os.path.exists("dantri.json") and os.path.getsize("dantri.json") > 0:
	with open('dantri.json', encoding="utf-8") as f:
		file_dantri = json.load(f)
		# clear duplicated items
		temp = []
		dup = 0
		for x in range(len(file_dantri)):
			for y in range(len(file_dantri)):
				if x!=y and file_dantri[x]["title"] == file_dantri[y]["title"]:
					dup = 1
					break
			if dup == 1:
				continue
			else:
				temp.append(file_dantri[x])
			dup = 0
		file_dantri = list(temp)

	if os.path.exists("old_dantri.json") and os.path.getsize("old_dantri.json") > 0:	
		with open('old_dantri.json', encoding="utf-8") as f:
			file_old_dantri = json.load(f)
		for x in file_dantri:
			if x not in file_old_dantri:
				if x["tab"] == "the gioi" or x["tab"] == "kinh doanh" or x["tab"] == "bat dong san":
					file_temp.append(x)
	else:
		file_temp = list(file_dantri)
for x in range(len(file_temp)):
	file_temp[x]["link"] = file_temp[x]["link"][0]
	file_temp[x]["description"] = file_temp[x]["description"][0]
	file_temp[x]["date"] = file_temp[x]["date"][0]
	file_temp[x]["title"] = file_temp[x]["title"][0]
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

with open("update_news.json", "w") as f:
	json.dump(file_data, f, indent=4)

#######################################

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "NEWs"
msg['From'] = me
msg['To'] = you

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