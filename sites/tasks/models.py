from django.db import models
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = CKEditor5Field('Text')
    created_by = models.ForeignKey("users.Profile", on_delete=models.CASCADE, related_name='created_tasks',null=True)
    assigned_to = models.ManyToManyField("users.Profile", related_name='assigned_tasks')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    deadline = models.DateTimeField(blank=True, null=True)

def __str__(self):
        return self.title

class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='commentsList')
    author = models.ForeignKey("users.Profile", on_delete=models.CASCADE)
    text = CKEditor5Field('Text')
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.text