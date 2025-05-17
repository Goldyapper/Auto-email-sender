import smtplib, ssl
from time import localtime, strftime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "adam.a.parsons15@gmail.com"  #Sender email
receiver_email = "adam.a.parsons15@gmail.com"  # receiver email
#password = input("Type your password and press enter: ") # quaa vbjo lkym kpcd 
password = "quaa vbjo lkym kpcd"

message = MIMEMultipart("alternative")
message["Subject"] = "Python test"
message["From"] = sender_email
message["To"] = receiver_email

now = strftime("%H:%M:%S" +" on the " "%d/%m/%y", localtime()) #gets current time and formats it

text = """\
Hello!
Check out this link

This message is sent from Python
Sent at """ + now  # emails content

html = """\
<html>
    <body>
        <P>Hello!<br>
        <br>
        Check out this <a href="http://www.realpython.com">link</a>
        <br> 
        </p>
    </body>
</html>
"""
# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    print('attempting to send email')
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("email sent")