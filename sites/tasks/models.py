from django.db import models
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field

class Task(models.Model):
    title = models.CharField('Заголовок',max_length=200)
    description = CKEditor5Field('Описание')
    created_by = models.ForeignKey("users.Profile",verbose_name='Кем создана Задача?', on_delete=models.CASCADE, related_name='created_tasks',null=True)
    assigned_to = models.ManyToManyField("users.Profile",verbose_name='Для кого создана Задача?',related_name='assigned_tasks')
    created_at = models.DateTimeField("Дата создания",default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    completed = models.BooleanField('Задача выполнена?',default=False)
    deadline = models.DateTimeField('Сроки выполнения',blank=True, null=True)
    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['title']
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='commentsList')
    author = models.ForeignKey("users.Profile",verbose_name='Автор', on_delete=models.CASCADE)
    text = CKEditor5Field('Коментарий')
    created_at = models.DateTimeField("Дата создания",default=timezone.now)
    def __str__(self):
        return self.text
    
    class Meta:
        ordering = ['task']
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'