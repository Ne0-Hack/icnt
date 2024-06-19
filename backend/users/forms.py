from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("login", "email", "age", "first_name", "last_name", "country", "phone", "password")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("login", "email", "age", "first_name", "last_name", "country", "phone", "password")
