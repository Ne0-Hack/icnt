import datetime
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from slugify import slugify
from users.models import CustomUser


class Service(models.Model):
    title = models.CharField(verbose_name="Название", max_length=255)
    description = RichTextUploadingField(verbose_name="Описание", config_name='article')
    image = models.ImageField("Изображение", upload_to='services/%Y_%m_%d/', blank=True)
    image_card = models.ImageField("Изображение для карточки", upload_to='services/%Y_%m_%d/', blank=True)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(verbose_name="Создано", auto_now=True)

    class Meta:
        verbose_name_plural = "Услуги"
        verbose_name = "Услуга"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.title}-{datetime.datetime.now().timestamp()}", separator="-")
        super().save(*args, **kwargs)


class ServiceCategory(models.Model):
    service = models.ForeignKey(verbose_name="Услуга", to="Service", on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Название", max_length=255)
    price = models.IntegerField(verbose_name="Цена", default=0)

    class Meta:
        verbose_name_plural = "Категории услуги"
        verbose_name = "Категория услуги"

    def __str__(self):
        return f"{self.service.title} - {self.title}"


OrderStatus = (
    ('0', "Рассматривается"),
    ('1', "Выполняется"),
    ('2', "Выполнен"),
    ('3', "Отменён"),
)


class Order(models.Model):
    serviceCategory = models.ForeignKey(verbose_name="Категория заказа", to="ServiceCategory", on_delete=models.CASCADE)
    customer = models.ForeignKey(verbose_name="Заказчик", to=CustomUser, on_delete=models.CASCADE)
    description = models.TextField(verbose_name="Примечание к заказу", max_length=4056)
    deadline = models.DateField(verbose_name="Дедлайн")
    status = models.CharField(verbose_name="Статус заказа", max_length=255, choices=OrderStatus, default=0)

    class Meta:
        verbose_name_plural = "Заказы"
        verbose_name = "Заказ"

    def __str__(self):
        return f"Заказ от {self.customer.login}"

    def status_progress(self):
        self.status = OrderStatus[1][0]
        self.save()

    def status_canceled(self):
        self.status = OrderStatus[3][0]
        self.save()

    def status_finished(self):
        self.status = OrderStatus[2][0]
        self.save()
