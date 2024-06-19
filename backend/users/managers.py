import random

from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):

    def create_user(self, login, password, first_name, last_name, age, country, email, phone, **extra_fields):
        if not login:
            raise ValueError(_("The Login must be set"))
        login = login.strip()
        if not first_name:
            raise ValueError(_("The Name must be set"))
        first_name = first_name.strip()
        if not last_name:
            raise ValueError(_("The Surname must be set"))
        last_name = last_name.strip()
        if not age:
            raise ValueError(_("The Age must be set"))
        age = age
        if not country:
            raise ValueError(_("The Country must be set"))
        country = country
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        if not phone:
            raise ValueError(_("The Phone must be set"))

        user = self.model(login=login, password=password, first_name=first_name, last_name=last_name, age=age,
                          country=country, email=email, phone=phone, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, login, password, email, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        extra_fields.setdefault("first_name", login)
        extra_fields.setdefault("last_name", login)
        extra_fields.setdefault("age", random.randrange(1, 99))
        extra_fields.setdefault("country", 1)
        extra_fields.setdefault("phone", random.randrange(1, 99))

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        if not login:
            raise ValueError(_("The Login must be set"))
        login = login.strip()
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.create_user(login=login, password=password, email=email, **extra_fields)
        return user
