from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('register.urls')),
    path('account/', include('account.urls')),
    path('calendar/',include('calendar_app.urls')),
    path('search/',include('search_app.urls')),
    path('reservation/',include('reservation.urls')),
    path('favorite/',include('favorite.urls')),
    path('chat/',include('chat.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + staticfiles_urlpatterns()
