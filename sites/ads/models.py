from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Advertisement(models.Model):
    photo = models.ImageField("Картинка", upload_to="ads/photo", null=True)
    title = models.CharField('Заголовок',max_length=255)
    description = CKEditor5Field('Описание',null=True)
    importance = models.IntegerField('Важность',choices=((1, 'Low'), (2, 'Medium'), (3, 'High')), default=1)
    is_published = models.BooleanField('Опубликовать?',default=False)
    publication_date = models.DateTimeField('Дата публикации',null=True, blank=True)
    send_email_notification = models.BooleanField('Отправить на Email уведомление?',default=False)
    send_telegram_notification = models.BooleanField('Отправить на TG уведомление?',default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_phot(self):
        if self.photo:
            return self.photo.url
        else:
            return '/static/images/profile-img.jpg'

    def __str__(self):
        return str(self.title)


    class Meta:
        ordering = ['title']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'