import os
from celery import Celery
from core.security import backend_security

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.develop')
print(backend_security.CELERY_BROKER_URL)
app = Celery('core', broker=backend_security.CELERY_BROKER_URL, broker_connection_retry_on_startup=True)

app.conf.enable_utc = False
app.conf.timezone = 'UTC'

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks([])


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
