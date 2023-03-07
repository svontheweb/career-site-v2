import os
import requests

# send application confirmation mail to organisation AND applicant
def send_mail(mail_to_id, mail_to_name):
      # Set your Mailgun API key and domain
      api_key = 'YOUR_API_KEY'
      domain = 'YOUR_DOMAIN_NAME'
      
      # Define your email parameters
      sender = 'sender@example.com'
      recipient = 'recipient@example.com'
      subject = 'Test Email'
      body = 'This is a test email sent via Mailgun API'
      
      # Make the API request to Mailgun
      response = requests.post(
          f"https://api.mailgun.net/v3/{domain}/messages",
          auth=("api", api_key),
          data={"from": sender,
                "to": recipient,
                "subject": subject,
                "text": body})
      
      # Check the status code of the API response
      if response.status_code == 200:
          print('Email sent successfully!')
      else:
          print('An error occurred while sending the email.')
          print(response.text)
  