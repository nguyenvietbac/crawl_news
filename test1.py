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

#######################################
file_data = []
#############################################
file_temp = []
if os.stat("dantri.json").st_size != 0 :
	with open('dantri.json', encoding="utf-8") as f:
		file_dantri = json.load(f)
	with open('old_dantri.json', encoding="utf-8") as f:
		file_old_dantri = json.load(f)
	for x in file_dantri:
		if x not in file_old_dantri:
			file_temp.append(x)
for x in range(len(file_temp)):
	file_temp[x]["link"] = file_temp[x]["link"][0]
	file_temp[x]["description"] = file_temp[x]["description"][0]
	file_temp[x]["date"] = file_temp[x]["date"][0]
	file_temp[x]["title"] = file_temp[x]["title"][0]
file_data.extend(file_temp)

###############################################
# file_data.extend(file_dantri)
###############################################
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