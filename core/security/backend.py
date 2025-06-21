import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent

load_dotenv(f"{BASE_DIR}/envs/backend/.env")


class BackendSecurity:
    DJANGO_SETTINGS_MODULE = os.environ.get('DJANGO_SETTINGS_MODULE', "core.settings.develop")
    DJANGO_SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', "some_secret_key")

    REDIS_URL = os.environ.get('REDIS_URL')
    REDIS_KEY_PREFIX = os.environ.get('REDIS_KEY_PREFIX')

    CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL')

    TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
    TELEGRAM_CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')


backend_security = BackendSecurity()

