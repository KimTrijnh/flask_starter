import os
import psycopg2
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from config import Config
from flask_migrate import Migrate


convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

app = Flask(__name__)

app.config.from_object(Config)
metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(app, metadata=metadata)

migrate = Migrate(app, db)


# BLUEPRINTS REGISTRATION
from src.components.user.views import user_blueprint
app.register_blueprint(user_blueprint, url_prefix="/user")
