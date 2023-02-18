from django.db import models
from django.contrib.auth.models import User


class Achievement(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='achievements/')
    conditions = models.TextField()
    date_earned = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='achievements')

    def __str__(self):
        return self.title

class UserAchievement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_achievements')
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE, related_name='achievement_users')
    date_earned = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'achievement')

    def __str__(self):
        return f'{self.user.username} - {self.achievement.title}'

class UserAchievementProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='achievement_progress')
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE, related_name='user_progress')
    date_completed = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f'{self.user.username} - {self.achievement.title}'