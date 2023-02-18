from django.db import models
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class FAQ(models.Model):
    question = CKEditor5Field('Вопрос')
    answer = CKEditor5Field('Ответ',null=True)

    def __str__(self):
        return str(self.question)

    class Meta:
        ordering = ['question']
        verbose_name = 'Вопрос-Ответ'
        verbose_name_plural = 'Вопросы-Ответы'