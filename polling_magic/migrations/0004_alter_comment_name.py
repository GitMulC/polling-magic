# Generated by Django 3.2.13 on 2022-05-26 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polling_magic', '0003_auto_20220522_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=80),
        ),
    ]
