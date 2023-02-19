from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.utils import timezone


class KnowledgeBase(models.Model):
    title = models.CharField('Заголовок',max_length=255)
    description = CKEditor5Field('Описание')
    photo = models.ImageField("Фото", upload_to="image/knowledge/photo/", null=True, blank=True)
    file = models.FileField('Загрузить файл',upload_to='knowledgebase/', null=True, blank=True)
    created_at = models.DateTimeField("Дата создания",default=timezone.now)
    created_by = models.ForeignKey("users.Profile",verbose_name='Кем создано?', on_delete=models.CASCADE, related_name='created',null=True)
    category = models.ForeignKey("users.Department", verbose_name="Категория",
                                 on_delete=models.CASCADE, related_name="knowledgebase", null=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['title']
        verbose_name = 'База знаний'
        verbose_name_plural = 'База знаний'