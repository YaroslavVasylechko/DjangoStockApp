from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_1_login.urls')),
    path('getinfo/', include('app_2_web.urls')),
]
