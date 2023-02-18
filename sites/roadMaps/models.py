from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from django.utils.crypto import get_random_string


class guideActionCategoria(models.Model):
    title = models.CharField("Название", max_length=50)
    
    class Meta:
        ordering = ['title']
        verbose_name = 'Карта'

class guideAction(models.Model):
    category = models.ForeignKey(guideActionCategoria, on_delete=models.CASCADE, null=True)
    order_count = models.IntegerField("Сортировка", default=0, editable=False)
    title = models.CharField("Заголовок", max_length=50)
    text=CKEditor5Field('Text')
    bigBox = models.BooleanField("Сделать поле основным?", default=True)
    required = models.BooleanField("Необходимый чек поинт?", default=True)

    class Meta:
        ordering = ['category', 'order_count']
        verbose_name = 'Карта'


    def save(self, *args, **kwargs):
        if not self.order_count:
            max_order_count = guideAction.objects.filter(category=self.category).aggregate(Max('order_count'))['order_count__max']
            if max_order_count is None:
                max_order_count = 0
            self.order_count = max_order_count + 1

        super(guideAction, self).save(*args, **kwargs)

