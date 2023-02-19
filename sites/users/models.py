from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from tasks.models import Task

class Department(models.Model):
    title = models.CharField("Название", max_length=50)
    
    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['title']
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'
class Profile(models.Model):
    ROLS_CHOICES = (
        ("NC", "Стажёр"),
        ("HR", "HR"),
        ("DIR", "Руководитель"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField("Фото", upload_to="image/profile/photo/", null=True, blank=True)
    city = models.CharField('Город',max_length=200,null=True)
    post = models.CharField('Должность',max_length=200,null=True)
    department = models.ForeignKey(Department, verbose_name="Отдел",related_name='profiles', on_delete=models.CASCADE, null=True)
    manager =models.BooleanField('Является руководством?',default=False)
    rols = models.CharField(max_length=10, choices=ROLS_CHOICES, default="NC")
    phone = models.CharField(max_length=20, default='+7')
    telegram_id = models.CharField(max_length=50, blank=True)
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
    def calculate_speed(self):
        total_time = 0
        num_completed = 0
        tasks = Task.objects.filter(employees=self.employee, status='done')
        for task in tasks:
            if task.start_time and task.end_time:
                total_time += (task.end_time - task.start_time).seconds
                num_completed += 1
        if num_completed > 0:
            self.speed = total_time / num_completed
        else:
            self.speed = 0

    def calculate_completion_rate(self):
        num_total = self.num_assigned
        if num_total > 0:
            self.completion_rate = self.num_completed / num_total * 100
        else:
            self.completion_rate = 0

    def calculate_avg_speed(self):
        num_completed = self.num_completed
        if num_completed > 0:
            self.avg_speed = self.speed * num_completed / self.num_assigned
        else:
            self.avg_speed = 0

    def update_metrics(self):
        self.calculate_speed()
        self.calculate_completion_rate()
        self.calculate_avg_speed()
        self.save()

    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
