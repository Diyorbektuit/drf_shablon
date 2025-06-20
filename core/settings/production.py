from .base import *

REST_FRAMEWORK.update({
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
})

DEBUG = False
ALLOWED_HOSTS = []

# CSRF and CORS
CSRF_TRUSTED_ORIGINS = []

CORS_ALLOW_HEADERS = [
    "authorization",
    "content-type",
    "x-csrftoken",
    "accept",
    "origin",
    "user-agent",
]

CORS_ALLOW_METHODS = [
    "GET",
    "POST",
    "PUT",
    "DELETE",
    "PATCH",
    "OPTIONS",
]

CORS_ALLOWED_ORIGINS = []

CSRF_COOKIE_SECURE = True  # Faqat HTTPS uchun ishlaydi
SESSION_COOKIE_SECURE = True  # Sessiya cookie'lari ham faqat HTTPS uchun
CORS_ALLOW_CREDENTIALS = True  # Credential (cookie) so'rovlari uchun
CORS_ALLOW_ALL_ORIGINS = False  # Xavfsizlik uchun True bo'lishi kerak emas