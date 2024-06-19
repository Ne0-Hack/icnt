import datetime
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from users.models import CustomUser
from slugify import slugify

ReviewStatus = (
    ('0', "На рассмотрении"),
    ('1', "Одобрено"),
    ('2', "Отказано"),
)


class Review(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=255)
    text = models.TextField(verbose_name="Отзыв", max_length=4056)
    user = models.ForeignKey(verbose_name="Пользователь", to=CustomUser, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, choices=ReviewStatus, default=0)
    created_at = models.DateTimeField(verbose_name="Создано:", auto_now_add=True)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return f"Отзыв от {self.user.login}"

    def status_accept(self):
        self.status = ReviewStatus[1][0]
        self.save()

    def status_deceline(self):
        self.status = ReviewStatus[2][0]
        self.delete()


class Article(models.Model):
    image = models.ImageField(verbose_name="Изображение", upload_to='article/%Y_%m_%d/', blank=True)
    title = models.CharField(verbose_name="Название новости", max_length=255)
    author = models.CharField(verbose_name="Автор", max_length=255)
    description = RichTextUploadingField(verbose_name="Текст новости", config_name='article')
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(verbose_name="Создано:", auto_now_add=True)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.title}-{datetime.datetime.now().timestamp()}", separator="-")
        super().save(*args, **kwargs)


class Works(models.Model):
    title = models.CharField(verbose_name="Название", max_length=255)
    subtitle = models.CharField(verbose_name="Короткое описание", max_length=255)
    imageA = models.ImageField(verbose_name="Изображение на верхнем плане", upload_to='works/%Y/%m/%d/', blank=True)
    imageB = models.ImageField(verbose_name="Изображение на нижнем плане", upload_to='works/%Y/%m/%d/', blank=True)
    tags = models.ManyToManyField(verbose_name="Тэги", to="WorksTags", blank=True)

    class Meta:
        verbose_name = "Работа"
        verbose_name_plural = "Работы"

    def __str__(self):
        return self.title


class WorksTags(models.Model):
    title = models.CharField(verbose_name="Тэг", max_length=255)

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"

    def __str__(self):
        return self.title


class WorksTasks(models.Model):
    work = models.ForeignKey(Works, on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Название выполненой задачи", max_length=255)

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    def __str__(self):
        return self.work.title + " - " + self.title
