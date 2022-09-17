# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import login_view, register_user
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/jwt/', view=obtain_auth_token),
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('social_login/', include('allauth.urls')),
]
