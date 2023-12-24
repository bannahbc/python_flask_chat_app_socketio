from main import db


class UserTable(db.Model):
    _id = db.Column("id",db.Integer,primary_key=True)
    name = db.Column("name",db.String(200))
    email = db.Column(db.String(200),unique = True)
    password = db.Column(db.String(200))


    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password = password


    def to_dict(self):
        data ={

        }


class Room(db.Model):
    _id = db.Column('id',db.Integer,primary_key=True)
    user_id = db.Column(db.Integer)
    room_id = db.Column(db.String(200))

    def __init__(self,user_id,room_id):
        self.user_id = user_id
        self.room_id = room_id