from shutil import register_unpack_format
from flask import Blueprint

views = Blueprint('views', __name__)

@views.route("/")
def home():
    return "Hello"
