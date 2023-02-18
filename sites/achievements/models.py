from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field

class Achievement(models.Model):
    title = models.CharField(max_length=100)
    description = CKEditor5Field('Описание',null=True)
    image = models.ImageField(upload_to='achievements/')
    conditions = CKEditor5Field('Коментарий',null=True)
    date_earned = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='achievements')


    def get_photo(self):
        if self.image:
            return self.image.url
        else:
            return '/static/images/profile-img.jpg'
        
    def __str__(self):
        return self.title

class UserAchievement(models.Model):
    user = models.ForeignKey("users.Profile", on_delete=models.CASCADE, related_name='user_achievements')
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE, related_name='achievement_users')
    date_earned = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'achievement')

    def __str__(self):
        return f'{self.user} - {self.achievement.title}'
