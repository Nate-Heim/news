# Nate Heim
# 10/13/2024
# pages/views.py

# importing modules
from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"
