from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/signup', admin.site.urls),
    path('', include('authentication.urls')),
]
