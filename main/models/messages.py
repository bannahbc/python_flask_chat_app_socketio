from main import db


class Messages(db.Model):
    _id = db.Column(db.Integer,primary_key=True)
    messages = db.Column(db.String(400))
    fro_m = db.Column(db.String(300))
    to = db.Column(db.String(300))
    current_time = db.Column(db.String(300))



    def __init__(self,messages,fro_m,to,current_time):
        self.messages = messages
        self.fro_m = fro_m
        self.to = to
        self.current_time = current_time
        