# Generated by Django 3.2.10 on 2022-01-23 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_basicpython'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicpython',
            name='image',
            field=models.ImageField(upload_to='pythonimg/pythonimg'),
        ),
    ]
