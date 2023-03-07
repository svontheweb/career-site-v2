from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import ssl
import os



def send_mail(mail_to_id, mail_to_name):
  # msg['From'] = 'Sender Name <sender@example.com>'
  # msg['To'] = 'Receiver Name <receiver@example.com>'
  mail_from_id = 'svontheweb@gmail.com'
  mail_from_name = 'Sujeet Verma'
  mail_from_pass = 'iqawygegkkzzxwqg'

  message = MIMEMultipart('alternative')
  message['Subject'] = "Application submitted!!"
  message['From'] = '{} <{}>'.format(mail_from_name, mail_from_id)
  message['To'] = '{} <{}>'.format(mail_to_name, mail_to_id)

  text = "Application submitted!!"
  html = """<h3>This is job-list site is a hobby project of <a href=\"https://github.com/svontheweb\"> Sujeet Verma </a> I am glad you used it :)</h3><br />We are happy to inform you that we have received your application for the role. <br><br>

Our team is currently reviewing your application and will be in touch with you soon regarding the next steps of the recruitment process. We appreciate the time and effort you have put into submitting your application. <br>

If you have any further questions or concerns, please feel free to reach out to us."""


  text_part = MIMEText(text, 'plain')
  html_part = MIMEText(html, 'html')

  message.attach(text_part)
  message.attach(html_part)

  context = ssl.create_default_context()

  with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
      smtp.login(mail_from_id, mail_from_pass)
      smtp.sendmail(mail_from_id, mail_to_id, message.as_string())







def send_mail_to_hr(mail_to_id, mail_to_name):
  # msg['From'] = 'Sender Name <sender@example.com>'
  # msg['To'] = 'Receiver Name <receiver@example.com>'
  mail_from_id = os.environ['SENDER_EMAIL']
  mail_from_name = 'HR Team'
  mail_from_pass = os.environ['SENDER_PASSWORD']

  message = MIMEMultipart('alternative')
  message['Subject'] = "A new application has been received!!"
  message['From'] = '{} <{}>'.format(mail_from_name, mail_from_id)
  message['To'] = '{} <{}>'.format('Hiring Manager', mail_from_id)

  text = "A new application has been received!!"
  html = """<html>
  <body>
      <h3>This is job-list site is a hobby project of <a href=\"https://github.com/svontheweb\">Sujeet Verma</a>.</h3>
      <br>
      <p>Dear Team,</p>
      <p>An application is received for a job listed on our site with the following details:</p>
      <ul>
          <li>APPLICANT NAME: {}</li>
          <li>APPLICANT EMAIL: {}</li>
      </ul>
      <p>If you have any further questions or concerns, please feel free to reach out to us.</p>
  </body>
  </html>""".format(mail_to_name, mail_to_id)


  text_part = MIMEText(text, 'plain')
  html_part = MIMEText(html, 'html')

  message.attach(text_part)
  message.attach(html_part)

  context = ssl.create_default_context()

  with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
      smtp.login(mail_from_id, mail_from_pass)
      smtp.sendmail(mail_from_id, mail_from_id, message.as_string())


