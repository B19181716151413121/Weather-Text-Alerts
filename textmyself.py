#Texting part, used Twilio
accountSID= '' #Enter account SID
authToken= '' #Enter account Token
myTwilioNumber='' #Enter Twilio number
actualPhone='' #Enter Your phone number

#Section that sends the text message
from twilio.rest import TwilioRestClient
def textmyself(message):
    twilioCli=TwilioRestClient(accountSID,authToken)
    twilioCli.messages.create(body=message,from_=myTwilioNumber,to=actualPhone)
