FROM python:3.10-slim

WORKDIR /app

# Zaruriy paketlarni o'rnatish va keshni tozalash
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential \
    && rm -rf /var/lib/apt/lists/*

# Kutubxonalarni o'rnatish
COPY ../../../requirements /app/requirements
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r /app/requirements/develop.txt \
    && pip cache purge

# Kodni va konfiguratsiya faylini ko'chirish
COPY . . .

# Portni ochish
EXPOSE 8000

# Gunicorn konfiguratsiya faylidan foydalanish
CMD ["gunicorn", "-c", "/app/deployment/gunicorn/gunicorn_develop.conf.py", "core.wsgi:application"]
