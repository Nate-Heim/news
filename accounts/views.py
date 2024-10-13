# Nate Heim
# Date: 10/13/2024
# Description: This is the views file for the accounts app.
# This file is used to define views for the accounts app.

# accounts/views.py

from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


# Create your views here.
