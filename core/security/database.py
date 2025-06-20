import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent

load_dotenv(f"{BASE_DIR}/envs/database/.env")


class DatabaseSecurity:
    ENGINE = os.environ.get('DB_ENGINE')
    NAME = os.environ.get('DB_NAME')
    USER = os.environ.get('DB_USER')
    PASSWORD = os.environ.get('DB_PASSWORD')
    HOST = os.environ.get('DB_HOST')
    PORT = os.environ.get('DB_PORT')


database_security = DatabaseSecurity()

