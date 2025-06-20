from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from core.schema import swagger_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
        *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
        *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
    ]
    urlpatterns += swagger_urlpatterns