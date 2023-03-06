"""
This call sends a message to one recipient.
"""
from mailjet_rest import Client
import os

# send application confirmation mail to organisation AND applicant
def send_mail(mail_to_id, mail_to_name):
  mail_from_id = 'svontheweb@gmail.com'
  mail_from_name = 'Sujeet Verma'
  # mailjet email confirmation keys
  API_KEY = os.environ['MJ_APIKEY_PUBLIC']
  SECRET_KEY = os.environ['MJ_APIKEY_PRIVATE']
  
  # api_key = os.environ['MJ_APIKEY_PUBLIC']
  # api_secret = os.environ['MJ_APIKEY_PRIVATE']
  mailjet = Client(auth=(API_KEY, SECRET_KEY), version='v3.1')

  # mail to organisation
  data = {
    'Messages': [
  				{
  						"From": {
  								"Email": mail_from_id,
  								"Name": mail_from_name
  						},
  						"To": [
  								{
  										"Email": mail_from_id,
  										"Name": mail_from_name
  								}
  						],
  						"Subject": "An application has been received",
  						"TextPart": "Dear Team  An application is received for job listed on our site.",
  						"HTMLPart": """<h3>This is job-list site is a hobby project of <a href=\"https://github.com/svontheweb\"> Sujeet Verma </a> I am glad you used it :)</h3><br />Dear Team<br>  An application is received for job listed on our site with followig details.<br>
        APPLICANT NAME: {} <br>
        APPLICANT EMAIL: {} 
<br><br>
If you have any further questions or concerns, please feel free to reach out to us""".format(mail_to_name, mail_to_id)
  				}
  		]
  }
  result = mailjet.send.create(data=data)

  # mail to applicant
  data = {
    'Messages': [
  				{
  						"From": {
  								"Email": mail_from_id,
  								"Name": mail_from_name
  						},
  						"To": [
  								{
  										"Email": mail_to_id,
  										"Name": mail_to_name
  								}
  						],
  						"Subject": "Your application has been received",
  						"TextPart": "Dear applicant  Welcome to our organisation!",
  						"HTMLPart": """<h3>This is job-list site is a hobby project of <a href=\"https://github.com/svontheweb\"> Sujeet Verma </a> I am glad you used it :)</h3><br />We are happy to inform you that we have received your application for the role. <br><br>

Our team is currently reviewing your application and will be in touch with you soon regarding the next steps of the recruitment process. We appreciate the time and effort you have put into submitting your application. <br>

If you have any further questions or concerns, please feel free to reach out to us"""
  				}
  		]
  }
  result = mailjet.send.create(data=data)
