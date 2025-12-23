import mysql.connector
from ..config import Config

def get_db_connection():
    try:
        return mysql.connector.connect(**Config.DB_CONFIG)
    except Exception as e:
        print(f"Error DB: {e}")
        return None