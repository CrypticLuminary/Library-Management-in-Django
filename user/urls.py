from django.urls import path,include
from django.contrib.auth.views import LogoutView
from .views import *

app_name = "user"
urlpatterns = [
    path('register/',registrationForm, name="register"),
    path('login/',Userlogin, name="login"),
     path('logout/', LogoutView.as_view(), name='logout'),
]
