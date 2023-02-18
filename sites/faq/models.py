from django.db import models
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class FAQ(models.Model):
    question = CKEditor5Field('Вопрос')
    answer = CKEditor5Field('Ответ')
# Create your models here.
