from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Department(models.Model):
    title = models.CharField("Название", max_length=50)
    
    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['title']
        verbose_name = 'Отдел'

class Profile(models.Model):
    ROLS_CHOICES = (
        ("NC", "Стажёр"),
        ("HR", "HR"),
        ("DIR", "Руководитель"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField("Фото", upload_to="image/profile/photo/", null=True)
    department = models.ForeignKey(Department, verbose_name="Отдел", on_delete=models.CASCADE, null=True)
    rols = models.CharField(max_length=10, choices=ROLS_CHOICES, default="NC")
    phone = models.CharField(max_length=20, default='-')
    telegram_id = models.CharField(max_length=50, default='-')
    birthday = models.DateField("День рождение", auto_now=False, auto_now_add=False, null=True)
    start_work = models.DateField("Старт работы в компании испытательного срока", auto_now=False, auto_now_add=False, null=True)
    end_probation = models.DateField("Окончание испытательного срока", auto_now=False, auto_now_add=False, null=True)

    def __str__(self):
        return self.user.get_full_name()

    def get_photo(self):
        if self.photo:
            return self.photo.url
        else:
            return '/static/images/profile-img.jpg'

    class Meta:
        verbose_name_plural = 'Профили'
        verbose_name = 'Профиль'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
