from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.db.models.signals import post_save
from django.dispatch import receiver
from notification.management.commands.bot import send_message_to_telegram_chat
from users.models import Profile


class Notification(models.Model):
    ROLS_CHOICES = (
        ("NC", "Стажёр"),
        ("HR", "HR"),
        ("DIR", "Руководитель"),
    )
    title = models.CharField("Заголовок", max_length=250)
    text = CKEditor5Field('Text')
    call_day = models.IntegerField("Через сколько дней после регистрации пользователя сработает", default=7)
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

@receiver(post_save, sender=Notification)
def send_notification_to_telegram(sender, instance, **kwargs):
    users_with_role = Profile.objects.filter(rols=instance.rols)
    for user in users_with_role:
        send_message_to_telegram_chat(user.telegram_id, instance.title, instance.text)