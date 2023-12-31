import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from behave import *
import logging

logging.basicConfig(filename="amazonlog.log", format="%(asctime)s  %(levelname)s:%(message)s", level=logging.INFO)

@then('send email notification')
def step_impl(context):
    try:
        print("Task completed")
        sender = "hellojaned123@gmail.com"
        sender_password = "dariqfjgajewxtev"
        receiver = "hellojaned123@gmail.com"
        msg = MIMEMultipart()

        msg['From'] = sender
        msg['To'] = receiver
        msg['Subject'] = "The program was executed successfully"
        body = """<pre> 
    Task successful
    Link for the allure report: <a href="https://allure-reports-summerproject.netlify.app/">click here</a>
    </pre>"""
        msg.attach(MIMEText(body, 'html'))

        
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            sender = "hellojaned123@gmail.com"
            sender_password = "dariqfjgajewxtev"
            receiver = "hellojaned123@gmail.com"
            smtp.login(sender, sender_password)
            text = msg.as_string()
            smtp.sendmail(sender,receiver,text)
            logging.info("E-mail sent!")
    except:
        logging.error("Error occurred. Could not send e-mail")