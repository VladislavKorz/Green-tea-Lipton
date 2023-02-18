from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Notification(models.Model):
    ROLS_CHOICES = (
        ("NC", "Стажёр"),
        ("HR", "HR"),
        ("DIR", "Руководитель"),
    )
    title = models.CharField("Заголовок", max_length=250)
    text = CKEditor5Field('Text')
    call_day = models.IntegerField("Через сколько дней сработает", default=7)
    call_time = models.TimeField("В какое время сработает", auto_now=False, auto_now_add=False)
    rols = models.CharField("Роль сотрудника", max_length=10, choices=ROLS_CHOICES, default="NC")

    class Meta:
        ordering = ['title']
        verbose_name = 'Уведомления'

class NotificationUser(models.Model):
    user = models.ForeignKey("users.Profile", verbose_name="", on_delete=models.CASCADE)
    notification = models.ForeignKey("notification.Notification", verbose_name="", on_delete=models.CASCADE)
    send_datetime = models.DateTimeField("Дата отправки", auto_now=False, auto_now_add=False)
    send_status = models.BooleanField("Статус отправки", default=True)
    create = models.DateTimeField("Дата создания", auto_now=False, auto_now_add=True)

    