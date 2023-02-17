from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from django.utils.crypto import get_random_string


class guideAction(models.Model):
    order_count = models.IntegerField("Сортировка", unique=True, default=0)
    title = models.CharField("Заголовок", max_length=50)
    text=CKEditor5Field('Text')
    bigBox = models.BooleanField("Сделать поле основным?", default=True)
    required = models.BooleanField("Необходимый чек поинт?", default=True)

    class Meta:
        ordering = ['order_count']
        verbose_name = 'Карта'