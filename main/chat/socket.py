from flask_socketio import SocketIO,join_room,leave_room,send
from main.chat.users import db,session
from main.models.users import UserTable,Room
from main.models.messages import Messages




def handle_socket_events(socketio: SocketIO):
    @socketio.on("connect")
    def connect():
        session_user = session['user_id']
        room = Room.query.filter_by(user_id=session_user).first()
        join_room(room.room_id)
        print(room.room_id)
        print('connected!')


    @socketio.on('message')
    def handle_message(data):
        # session_user = session['user_id']
        # session_user_room_id = Room.query.filter_by(user_id=session_user).first()
        print("haipppppppppppppppp",data)
        if data['message']:
            new_msg = Messages(data['message'],data['sender'],data['receciver_room'],data['time'])
            db.session.add(new_msg)
            db.session.commit()
            print("message saved ! in socket")
            content = {
                'message':data['message'],
                'from':data['sender'],
                'to':data['receciver_room'],
                'time':data['time']
            } 
            send(content,to=data['sender'])
            send(content,to=data['receciver_room'])
            print("hello",content)

    @socketio.on("disconnect")
    def disconnect():
        session_user = session['user_id']
        room = Room.query.filter_by(user_id=session_user).first()
        leave_room(room.room_id)
        print("disconnected")