import ssl
import smtplib

from email.message import EmailMessage
from p1_all_emails import emails

# Add your email account and your password
email_sender = "your.email@gmail.com"
email_password = "your_password"

# Here will be all the emails address that you are going to send an email, the subject and the body.
email_receiver = emails
subject = "Hello"
body = """
Hello,

This is an email that was sent using Python.

Regards!
"""

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["Cc"] = email_receiver
em["Bcc"] = email_receiver
em["subject"] = subject
em.set_content(body)

# You can attach a file.
files = ["Your_File_Attached.docx"]
for file in files:
    with open(file, "rb") as f:
        file_data = f.read()
    em.add_attachment(file_data, maintype="application", subtype="octet-stream", filename="Your_File_Attached.docx")

# Configuring the protocols on how you will send the email
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())