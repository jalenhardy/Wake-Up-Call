from twilio.rest import Client


class Call:

    def __init__(self, account_sid, auth_token):
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.client = Client(self.account_sid, self.auth_token)

    def call(self):
        call = self.client.calls.create(to="6672315912", from_="6672315912", url="http://demo.twilio.com/docs/voice.xml")
        print(call.sid)
