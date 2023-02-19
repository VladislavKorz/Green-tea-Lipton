from django.db import models



class KnowledgeBase(models.Model):
    title = models.CharField('Заголовок',max_length=255)
    description = models.TextField('Описание',)
    file = models.FileField('Загрузить файл',upload_to='knowledgebase/', null=True, blank=True)
    category = models.ForeignKey("users.Department", verbose_name="Категория",
                                 on_delete=models.CASCADE, related_name="knowledgebase", null=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['title']
        verbose_name = 'База знаний'
        verbose_name_plural = 'База знаний'