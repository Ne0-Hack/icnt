from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import UserManager

country_list = (
    ('0', "Россия"),
    ('1', "Казахстан"),
    ('2', "Беларусь"),
)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = None

    login = models.CharField(_("Логин"), max_length=255, unique=True)
    first_name = models.CharField(_("Имя"), max_length=255, blank=True)
    last_name = models.CharField(_("Фамилия"), max_length=255, blank=True)
    age = models.IntegerField(_("Возраст"), default=1, blank=True)
    country = models.CharField(_("Страна"), max_length=255, blank=True, default=0, choices=country_list)
    email = models.EmailField(_("Почта"), unique=True)
    phone = models.CharField(_("Номер телефона"), max_length=20, unique=True, blank=True)
    user_photo = models.ImageField("Изображение", upload_to='users/%Y_%m_%d/', blank=True)

    is_staff = models.BooleanField("Является администратором?", default=False)
    is_superuser = models.BooleanField("Является суперпользователем?", default=False)
    is_active = models.BooleanField("Аккаунт активен?", help_text="Управляет блокировкой аккаунта", default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "login"
    REQUIRED_FIELDS = ["email"]

    objects = UserManager()

    def __str__(self):
        return self.login

    class Meta:
        verbose_name_plural = "пользователи"
        verbose_name = "пользователь"


class CustomGroup(Group):
    class Meta:
        verbose_name = _("group")
        verbose_name_plural = _("groups")
