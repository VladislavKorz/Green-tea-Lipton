# Generated by Django 4.1.7 on 2023-02-18 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roadMaps', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='guideaction',
            options={'ordering': ['department', 'order_count'], 'verbose_name': 'Карта', 'verbose_name_plural': 'Карты'},
        ),
    ]
