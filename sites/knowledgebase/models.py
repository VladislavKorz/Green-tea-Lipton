from django.db import models

class Category(models.Model):
    title = models.CharField("Название", max_length=50)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

class KnowledgeBase(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='knowledgebase/', null=True, blank=True)
    category = models.ForeignKey(Category, verbose_name="Категория",
                                 on_delete=models.CASCADE, related_name="questionList", null=True)
    def __str__(self):
        return self.title