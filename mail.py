# PGM to send e-mail using gmail

# -*- coding: utf-8 -*-
from smtplib         import SMTP_SSL
from email.header   import Header
from email.mime.text import MIMEText

#username & password
uname='********@gmail.com'
passwd = '*****'

# Message Details
message = MIMEText('Test mail from Python', _charset='utf-8')
message['Subject'] = Header('Test Mail', 'utf-8')
From = uname
To = '*********@gmail.com'

# gmail
s = SMTP_SSL('smtp.gmail.com', 465, timeout=10)

try:
    s.login(uname, passwd)
    s.sendmail(From, To, message.as_string())
finally:
    s.quit()
