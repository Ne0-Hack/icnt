# Generated by Django 5.0.4 on 2024-06-19 18:55

import django.contrib.auth.models
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomGroup',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.group')),
            ],
            options={
                'verbose_name': 'group',
                'verbose_name_plural': 'groups',
            },
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('login', models.CharField(max_length=255, unique=True, verbose_name='Логин')),
                ('first_name', models.CharField(blank=True, max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=255, verbose_name='Фамилия')),
                ('age', models.IntegerField(blank=True, default=1, verbose_name='Возраст')),
                ('country', models.CharField(blank=True, choices=[('0', 'Россия'), ('1', 'Казахстан'), ('2', 'Беларусь')], default=0, max_length=255, verbose_name='Страна')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Почта')),
                ('phone', models.CharField(blank=True, max_length=20, unique=True, verbose_name='Номер телефона')),
                ('user_photo', models.ImageField(blank=True, upload_to='users/%Y_%m_%d/', verbose_name='Изображение')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Является администратором?')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Является суперпользователем?')),
                ('is_active', models.BooleanField(default=True, help_text='Управляет блокировкой аккаунта', verbose_name='Аккаунт активен?')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'пользователь',
                'verbose_name_plural': 'пользователи',
            },
        ),
    ]
