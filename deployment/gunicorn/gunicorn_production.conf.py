import multiprocessing
from core.settings.base import BASE_DIR

# Server sozlamalari
bind = "0.0.0.0:8000"  # IP va portni belgilang
workers = multiprocessing.cpu_count() * 2 + 1  # Ishchilar soni
threads = 2  # Har bir ishchi uchun mavzular
timeout = 30  # Sekundlarda taym-aut

# Kirish fayllari
loglevel = "info"  # Loglar darajasi
accesslog = f"{BASE_DIR}/gunicorn_access_logs"  # Kirish loglari konsolga
errorlog = f"{BASE_DIR}/gunicorn_error_logs"  # Xatolik loglari konsolga

# Maksimal so'rovlar hajmi (byte)
limit_request_line = 4094  # Maksimal so'rov satri uzunligi
limit_request_fields = 100  # Maksimal so'rov sarlavhalari
limit_request_field_size = 8190  # Maksimal sarlavha uzunligi
