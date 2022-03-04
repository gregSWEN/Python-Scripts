import smtplib 
import ssl
from email.message import EmailMessage 


subject = "Email From Python"
body = "This is a test email from python"
sender_email = "gregvillafane1@gmail.com"
receiver_email = "gregvillafane1@gmail.com"
password = input("Enter a password: ")

#instantiate the email mesage class 
message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject


html = f"""
<html>
    <body>
        <h1>{subject}</h1>
        <p>{body}</p>
    </body>
</html>
"""

message.add_alternative(html, subtype="html")

#when we connect to gmail, we need a secure connection. This gives us a context for a secure connectrin 
# We dont have our own mail server we are connecting to the default gmail one 
context = ssl.create_default_context()


print("Sending Email!")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    #We can also read emails 
    server.sendmail(sender_email, receiver_email, message.as_string())


print("Success")