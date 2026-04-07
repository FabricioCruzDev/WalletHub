import sqlite3
from dotenv import dotenv_values
import os

# Load environment variables from .env
config = dotenv_values(".env")

DB = config["LOCAL_DB_PATH"]

conn = sqlite3.connect("db_wallet.db")
cur = conn.cursor()

query = """DROP TABLE teste"""

cur.execute(query)


