from flask_restful import Api
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    api = Api(app, prefix="/api/v1")
    db.init_app(app)

    from app.resources.contacts import Contacts
    api.add_resource(Contacts, "/contacts")

    from app.resources.auth import Login, Register
    api.add_resource(Login, "/login")
    api.add_resource(Register, "/register")

    return app