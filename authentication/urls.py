from django.contrib import admin
from django.urls import path, include
from authentication import views as auth_views

urlpatterns = [
    path('', auth_views.home, name='home'),
    path('signup/', auth_views.signup, name='signup'),
    path('signin/', auth_views.signin, name='signin'),
    path('signout/', auth_views.signout, name='signout'),
    path('activate/<uidb64>/<token>/', auth_views.activate, name='activate'),
]