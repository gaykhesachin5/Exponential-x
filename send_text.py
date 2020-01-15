import smtplib
from email.mime.text import MIMEText

smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
smtp_ssl_port = 465
username = 'gaykhesachin5@gmail.com'
password = 'Sachin@5268'
sender = 'gaykhesachin5@gmail.com'
targets = ['gaykhesachin5@gmail.com', 'sachintechedu5@gmail.com']

msg = MIMEText('Hi, how are you today?')
msg['Subject'] = 'Hello'
msg['From'] = sender
msg['To'] = ', '.join(targets)

server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
server.login(username, password)
server.sendmail(sender, targets, msg.as_string())
server.quit()