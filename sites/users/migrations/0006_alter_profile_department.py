# Generated by Django 4.1.7 on 2023-02-19 01:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_phone_alter_profile_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to='users.department', verbose_name='Отдел'),
        ),
    ]
