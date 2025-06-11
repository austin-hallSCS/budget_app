from os import path, environ
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

# Base config
class Config:
    SECRET_KEY= environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{path.join(basedir, 'database.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DATAFOLDER = f"{path.join(basedir, 'data')}"