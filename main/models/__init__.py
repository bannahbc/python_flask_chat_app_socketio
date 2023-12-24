from flask import Blueprint

bp = Blueprint('models',__name__)

from .messages import Messages
from .users import UserTable,Room
