# Generated by Django 4.1.7 on 2023-02-19 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knowledgebase', '0004_alter_knowledgebase_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='knowledgebase',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='image/knowledge/photo/', verbose_name='Фото'),
        ),
    ]
