import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Kaushal Sharma'
email['to'] = 'sharmakaushal.er@gmail.com'
email['subject'] = 'YOU HAVE WON 100000 DOLLARS!'

email.set_content(html.substitute({'name': 'Tintin'}),'html')

with smtplib.SMTP(host='smtp.gmail.com',port= 587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('sharmakaushal.er@gmail.com','12345')
	smtp.send_message(email)
	print('all good boss!')


