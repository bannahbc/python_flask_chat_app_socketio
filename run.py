from main import app_create,db


app = app_create()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.socketio.run(app, debug=True,port=7000)