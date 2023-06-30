
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from feed import urls as feed_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(feed_urls, namespace = 'feed'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    
