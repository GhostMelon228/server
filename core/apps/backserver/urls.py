from django.contrib import admin
from django.urls import path

from core.apps.backserver.views import UserRegistrationView, UserLoginView, UserLogoutView, MainPageView

urlpatterns = [
    path('registration/', UserRegistrationView.as_view(), name='UserRegistration'),
    path('login/', UserLoginView.as_view(), name='Login'),
    path('logout/', UserLogoutView.as_view(), name='Logout'),

    path('users/homepage/', MainPageView.as_view(), name='home'),
]