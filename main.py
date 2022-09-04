"""
Extract birthday dates and send them per mail
"""
import smtplib
import ssl
from Secret.const import *


smtpobj = smtplib.SMTP(SMTP_Server, port)
subject = "Verjaardag kalender komende verjaardagen"
message = """
Hello,
Is it me your looking for?
"""

#context = ssl.create_default_context()
with smtplib.SMTP(SMTP_Server, port) as server:
    server.login(mail_adress, mail_password)
    server.sendmail(mail_adress, receiver_email, message)
    server.quit()
