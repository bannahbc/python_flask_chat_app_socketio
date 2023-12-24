from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO


db = SQLAlchemy()

def app_create():
    app = Flask(__name__)
    # export FLASK_APP=your_module_name:app
    # export FLASK_ENV=development  # Optional, but recommended for development

    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///UserTable.sqlite3"
    app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
    app.secret_key = "jaguar"
    

    socketio = SocketIO(app)
    
    
    from main.chat.socket import handle_socket_events
    handle_socket_events(socketio)

    from main.chat import bp as main_bp
    app.register_blueprint(main_bp)
    
    from main.models import bp as model_bp
    app.register_blueprint(model_bp)
    
    db.init_app(app)
    app.socketio = socketio
    return app