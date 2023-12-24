from . import bp
from flask import render_template,request,session,flash,redirect,url_for
from werkzeug.security import generate_password_hash,check_password_hash
from main.models.users import UserTable,db,Room
import random,string


@bp.route("/",methods=['GET','POST'])
@bp.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = UserTable.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password,password):
                session['email'] = user.email
                session['user_id'] = user._id
                print(session['email'])
                return redirect(url_for('main.home'))
    return render_template("login.html")


@bp.route("/register",methods=['GET','POST'])
def register():

    if request.method == 'POST':
        email = request.form["email"]
        print(email,"ldskajfkjdskf")
        user_name = request.form["user_name"]
        password = request.form["password"]
        print(email,user_name,password)
        hashed_pass = generate_password_hash(password)
        used_email = UserTable.query.filter_by(email=email).first()
        if used_email:
            flash("email already exist")
        else:
            new_user = UserTable(user_name,email,hashed_pass)
            print(new_user)
            db.session.add(new_user)
            db.session.commit()
            room_code = Room(new_user._id,''.join(random.choices(string.ascii_uppercase, k=5)))
            print("heoo",room_code)
            db.session.add(room_code)
            db.session.commit()
    return render_template("register.html")