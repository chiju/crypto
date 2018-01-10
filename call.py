import json,requests
import time
import base64

url = 'https://koinex.in/api/ticker'
url_sinch = 'https://callingapi.sinch.com/v1/callouts'

def send_email(user, pwd, recipient, subject, body):
    import smtplib

    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print 'successfully sent the mail'
    except Exception, e:
        print e

def makecall():
    payload = {'method': 'ttsCallout','ttsCallout': {'cli': 46000000000,
                #Change your number here.
               'destination': {'type': 'number', 'endpoint': '+91XXXXXXXXXXX'},
               'domain': 'pstn','custom': 'customData','locale': 'en-US',
               'prompts': '#tts[Ripple is changing];myprerecordedfile',
               'enabledice': True
               }}
    #Signup at sinch - create an app - verify your number to get 2$ credit, use app secret and key below. Dont pick the
    #call, picking the call will eat your balance, rejecting the call might promp two more calls fomr +1 111111
    #reject those calls as well.
    headers = {'Authorization':'Basic '+ base64.b64encode('app key'+':'+'appsecret'),
               'Content-Type':'application/json'}
    response = requests.post(url=url_sinch,data=json.dumps(payload),headers=headers)
    print response.text
while 1:
    try:
        resp = requests.get(url=url)
        data = json.loads(resp.text)

        print data['prices']['XRP']

        if float(data['prices']['XRP']) <= 160 or float(data['prices']['XRP']) >= 185:
            makecall()
            #enable if you want to send email, uses a gmail account. alter the smtp params in the method above
            #send_email('karthik.panicker@gmail.com','password for gmail account','karthik@attinadsoftware.com','KOINEX','XRP: '+data['prices']['XRP'])
    except Exception, e:
        print e
    time.sleep(20)
