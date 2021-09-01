import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Bericht in HTML
f = open('spam.html', 'r')
html = f.read()
htmlstage = MIMEText(html, "html")
message = str(htmlstage)


# Verzendlijst
to = ['daan@daanesmee.nl', 'slachtoffer1@daanesmee.nl', 'slachtoffer2@daanesmee.nl' , 'slachtoffer3@daanesmee.nl' , 'slachtoffer4@daanesmee.nl', 'esmee@daanesmee.nl']

# Server connectie
smtp_user = 'spam@daanesmee.nl'
smtp_pwd = 'Spammer123.'
smtpserver = smtplib.SMTP("mail.daanesmee.nl",587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(smtp_user, smtp_pwd)

# Mail opstellen
msg = MIMEMultipart('alternative')
msg.attach(htmlstage)
msg['Subject'] = "Dit is spam"
msg['From'] = smtp_user
msg['To'] = ", ".join(to)

# Mail verzenden en connectie verbreken
smtpserver.sendmail(smtp_user, to, msg.as_string())
smtpserver.close()