# Nate Heim

# pages/urls.py

# importing needed modules
from django.urls import path
from .views import HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
]
