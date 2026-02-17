from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import reminder_page , contact_submit_api

urlpatterns = [
    path('', reminder_page, name='reminder_page'),
    path('api/contact-submit/', contact_submit_api, name='contact_submit_api')
]

# Add static and media URLs for development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)