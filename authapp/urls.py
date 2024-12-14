from django.urls import path
from .views import login, register, logout, profile

urlpatterns = [
    path('login/', login),
    path('register/', register),
    path('logout/', logout),
    path('profile/', profile)
]
