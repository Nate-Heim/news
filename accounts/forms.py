# Nate Heim
# acoounts/forms.py

# importin
# g needed modules
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


# class creations
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "age",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "age",
        )
