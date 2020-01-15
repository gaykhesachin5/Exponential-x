import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import csv

sender_email = "username@gmail.com"
password = "userpassword"

# Create the plain-text and HTML version of your message
text = """
Hii.. <first_name> <last_name>
Wel-come to Lead Generation Automtion Tool.
"""

def main():
    try:
        reader = csv.DictReader(open("Something.csv"))
    except Exception as e:
        print(e)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        for raw in reader:
            fname = raw['First Name']
            lname = raw['Last Name']
            receiver_email = raw['Email']
            
            message = MIMEMultipart("alternative")
            message["Subject"] = "Demo Mail Sending"
            message["From"] = sender_email
            message["To"] = receiver_email
            text1=text.replace("<first_name>",fname)
            text1=text1.replace("<last_name>",lname)
            part1 = MIMEText(text1, "plain")
            message.attach(part1)
            server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
    print("Done..!")


if __name__ == "__main__":
    main()