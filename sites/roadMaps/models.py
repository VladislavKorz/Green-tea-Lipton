from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from django.utils.crypto import get_random_string
from loguru import logger

class guideAction(models.Model):
    department = models.ForeignKey("users.Department", on_delete=models.CASCADE, null=True)
    order_count = models.PositiveIntegerField("Сортировка", default=0, blank=False, null=False)
    title = models.CharField("Заголовок", max_length=50)
    text = CKEditor5Field('Text')
    bigBox = models.BooleanField("Сделать поле основным?", default=True)
    required = models.BooleanField("Необходимый чек поинт?", default=True)

    class Meta:
        ordering = ['department', 'order_count']
        verbose_name = 'Карта'
        verbose_name_plural = 'Карты'
    def get_absolute_url(self):
        return reverse("roadMapsSingle", kwargs={"pk": self.pk})
    

    def save(self, *args, **kwargs):
        if not self.order_count:
            max_order_count = guideAction.objects.filter(department=self.department).aggregate(Max('order_count'))['order_count__max']
            if max_order_count is None:
                max_order_count = 0
            self.order_count = max_order_count + 1
            
        super(guideAction, self).save(*args, **kwargs)



class UserguideAction(models.Model):
    user = models.ForeignKey("users.Profile", on_delete=models.CASCADE, related_name='user_guideActions')
    guideAction = models.ForeignKey(guideAction, on_delete=models.CASCADE, related_name='guideAction_users')
    date_earned = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'guideAction')

    def __str__(self):
        return f'{self.user} - {self.guideAction.title}'
    
    def get_count_of_actions(self):
        return self.user_guideActions.count()
