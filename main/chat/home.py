from main.chat import bp,db
from flask import render_template,session,request,redirect,url_for
from main.models.users import UserTable,Room
from main.models.messages import Messages
from main.chat.users import session
from datetime import datetime

@bp.route('/home',methods=['GET'])
def home():
    user_id = request.args.get('user_to') 
    chatting_user = UserTable.query.filter_by(_id=user_id).first()
    print("user",user_id)
    users = UserTable.query.all()
    from_room = Room.query.filter_by(user_id=session['user_id']).first()
    to_room = Room.query.filter_by(user_id=user_id).first()
    if user_id:
        print("tt",to_room.room_id,from_room.room_id)
        allMessages = Messages.query.filter(Messages.fro_m.in_([from_room.room_id,to_room.room_id]),Messages.to.in_([from_room.room_id,to_room.room_id])).all()
        print("mssg",allMessages)
        return render_template("home.html",users=users,user_in_session=session['email'],chatting_user=chatting_user,allMessages=allMessages,from_room=from_room,to_room=to_room)
    return render_template("home.html",users=users,user_in_session=session['email'],chatting_user=chatting_user,to_room=to_room,from_room=from_room)

@bp.route('/chat/<id>',methods=['GET','POST'])
def chat(id):
    print(id)
    # from_room = Room.query.filter_by(user_id=session['user_id']).first()
    # to_room = Room.query.filter_by(user_id=id).first()
    # allMessages = Messages.query.filter(Messages.fro_m.in_([from_room.room_id,to_room.room_id]),Messages.to.in_([from_room.room_id,to_room.room_id])).all()
    # messages_from = Messages.query.filter(Messages.fro_m.in_(from_room.room_id),Messages.to.in_(to_room.room_id)).all()
    # messages_to = Messages.query.filter(Messages.to.in_(from_room.room_id),Messages.fro_m.in_(to_room.room_id)).all()
    print("m")
    

    return redirect(url_for("main.home",user_to=id))

@bp.route("/save_messages",methods=['POST'])
def messages():
    data = request.get_json(force=True) or {}
    message = data.get('message')
    user_id = data.get('userId')
    if message:
        from_room = Room.query.filter_by(user_id=session['user_id']).first()
        to_room = Room.query.filter_by(user_id=user_id).first()
        new_message = Messages(message,from_room.room_id,to_room.room_id,datetime.now())
        db.session.add(new_message)
        db.session.commit()
        print("message saved!")
    
    return "hello"