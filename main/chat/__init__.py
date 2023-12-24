from flask.blueprints import Blueprint

bp = Blueprint('main',__name__,template_folder='templates',static_folder="static")

from main.chat.users import *
from main.chat.home import home,chat
from .socket import *