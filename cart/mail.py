import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



def send_mail(user,to, body):
    msg = MIMEMultipart()
    msg['From'] = 'levapython@yandex.ru'
    msg['To'] = str(to)
    msg['Subject'] = f'Заявка с сайта от {user}'
    message = body
    msg.attach(MIMEText(message))
    try:
        mailserver = smtplib.SMTP_SSL('smtp.yandex.ru',465)
        mailserver.set_debuglevel(True)
        mailserver.login('levapython@yandex.ru', 'dzwiiplfwzugzwdq')
        mailserver.sendmail('levapython@yandex.ru', to, msg.as_string())
        mailserver.quit()
        print("Письмо успешно отправлено")
    except smtplib.SMTPException:
        print("Ошибка: Невозможно отправить сообщение")

