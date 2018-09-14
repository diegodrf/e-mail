from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib

def sendEmail(user, password, to, subject, msg):
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    try:
        mail.ehlo_or_helo_if_needed()
        mail.starttls()
        mail.login(user, password)
        mail.sendmail(user, to, 'Subject: {}\n{}'.format(subject, msg.as_string()))

    except Exception as error:
        print('Falha ao enviar.\nErro: {}'.format(error))

    finally:
        mail.quit()


def email(user, password, to, subject, message, attachment=None):
    msg = MIMEMultipart()
    msg['From'] = user
    msg['Reply-to'] = to
    msg['Subject'] = subject
    part = MIMEText(message)
    msg.attach(part)
    if attachment is not None:
        msg.preamble = 'Multipart massage.\n'
        part = MIMEApplication(open(attachment, "rb").read())
        part.add_header('Content-Disposition', 'attachment', filename=attachment)
        msg.attach(part)

    else:
        pass

    sendEmail(user, password, to, subject, msg)