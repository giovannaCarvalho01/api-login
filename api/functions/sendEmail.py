import smtplib
import email.message
import dotenv
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

dotenv.load_dotenv()

# Envio pelo Gmail
def sendEmailGmail(token, sendEmail):
    corpo = f"""
    <p> <b>Token: <b> <p>
    <p> <b>{token}<b> <p>
    """
    
    msg = email.message.Message()
    msg['Subject'] = 'Token de Acesso APK Vendas'
    msg['From'] = os.getenv('EMAIL_GMAIL')
    msg['To'] = sendEmail

    password = os.getenv('PASSWORD_GMAIL')
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo)
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    
    # Login
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    
    return True

# Envio pelo Outlook    
def sendEmailOutlook(token, sendEmail):
    
    host = 'smtp-mail.outlook.com'
    port = '587'
    login = os.getenv('EMAIL_OUTLOOK')
    senha = os.getenv('PASSWORD_OUTLOOK')

    server = smtplib.SMTP(host, port)
    
    #Login
    server.ehlo()
    server.starttls()
    server.login(login, senha)
    
    body = f'Token de acesso: {token}'
    
    email_msg = MIMEMultipart()
    email_msg['FROM'] = login
    email_msg['To'] = sendEmail
    email_msg['Subject'] = 'Token - MVP Atan Vendas'
    
    email_msg.attach(MIMEText(body, 'Plain'))
    
    server.sendmail(email_msg['FROM'], email_msg['To'], email_msg.as_string())
    
    server.quit()
    return True