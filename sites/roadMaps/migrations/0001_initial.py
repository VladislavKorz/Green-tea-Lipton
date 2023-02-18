# Generated by Django 4.1.7 on 2023-02-17 21:58

from django.db import migrations, models
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='guideAction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_count', models.IntegerField(default=0, unique=True, verbose_name='Сортировка')),
                ('title', models.CharField(max_length=50, verbose_name='')),
                ('text', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text')),
                ('bigBox', models.BooleanField(default=True, verbose_name='Сделать поле основным?')),
                ('required', models.BooleanField(default=True, verbose_name='Необходимый чек поинт?')),
            ],
            options={
                'verbose_name': 'Карта',
                'ordering': ['order_count'],
            },
        ),
    ]