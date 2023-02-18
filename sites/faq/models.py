from django.db import models
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Category(models.Model):
    title = models.CharField("Название", max_length=50)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class FAQ(models.Model):
    question = CKEditor5Field('Вопрос')
    answer = CKEditor5Field('Ответ',null=True)
    category = models.ForeignKey(Category, verbose_name="Категория",
                                 on_delete=models.CASCADE, related_name="questionList", null=True)


    def __str__(self):
        return str(self.question)

    class Meta:
        ordering = ['question']
        verbose_name = 'Вопрос-Ответ'
        verbose_name_plural = 'Вопросы-Ответы'