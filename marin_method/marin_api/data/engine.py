#DATA ENGINE
# import psycopg2
from sqlalchemy.engine.base import Engine
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

from marin_api.data.models import BASE
from dotenv import dotenv_values

config = dotenv_values("this_is_not_an_env.txt")
engine: Engine = None

DBSession = sessionmaker()

def init_db():
    url = f"postgresql+psycopg2://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['dbname']}"
    if not database_exists(url):
        create_database(url)
    engine = create_engine(url)
    BASE.metadata.create_all(bind=engine)
    DBSession.configure(bind=engine)

