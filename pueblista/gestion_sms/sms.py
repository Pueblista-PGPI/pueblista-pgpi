from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

def send_sms(to, body):
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    from_ = os.getenv('TWILIO_PHONE_NUMBER')
    
    to = "+34" + to
    
    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
        to=to,
        from_=from_,
        body=body
    )
    
    print(message.body)
    
    
    