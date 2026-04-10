import sqlite3
from dotenv import dotenv_values
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Load environment variables from .env
config = dotenv_values(".env")

__DB = config["LOCAL_DB_PATH"]

#Conexão
engine = create_engine(__DB)

#Sessões
Session = sessionmaker(bind=engine)

#Base
Base = declarative_base()