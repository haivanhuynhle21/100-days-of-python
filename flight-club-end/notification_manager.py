import smtplib
from twilio.rest import Client

TWILIO_SID = "AC1f213138843cb4f37b76972bc091a0ac"
TWILIO_AUTH_TOKEN = "131576ae3cf4c1c2bb924daf3b741ac4"
TWILIO_VIRTUAL_NUMBER = '+13156591922'
TWILIO_VERIFIED_NUMBER = '+84849396669'
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "kemjau2032@gmail.com"
MY_PASSWORD = "gld9d038"

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )