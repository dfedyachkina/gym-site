# Generated by Django 5.1.4 on 2025-01-12 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym_home', '0002_alter_carousel_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carousel',
            name='description',
        ),
    ]
