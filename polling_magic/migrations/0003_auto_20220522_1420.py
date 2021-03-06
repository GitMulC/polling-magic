# Generated by Django 3.2.13 on 2022-05-22 14:20

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polling_magic', '0002_alter_comment_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='set image'),
        ),
        migrations.AlterField(
            model_name='poll',
            name='set_icon',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='set icon'),
        ),
    ]
