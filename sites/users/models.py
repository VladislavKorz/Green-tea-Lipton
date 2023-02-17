# from django.db import models
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver


# class Profile(models.Model):
#     ROLS_CHOICES = (
#         ("NC", "Стажёр"),
#         ("HR", "HR"),
#         ("DIR", "Стажёр"),

#     )
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     rols = models.CharField(max_length=9, choices=ROLS_CHOICES, default="NC")


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
