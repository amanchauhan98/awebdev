# Generated by Django 3.2.10 on 2022-01-22 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_basicpython'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicpython',
            name='img',
            field=models.ImageField(upload_to=''),
        ),
    ]