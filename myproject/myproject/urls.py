from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shops/', include('shops.urls')),  # Include URLs from shops app
]
