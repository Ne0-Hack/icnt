from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', views.obtain_auth_token),
    path('users/', include('users.urls')),
    path('contents/', include('contents.urls')),
    path('services/', include('services.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
