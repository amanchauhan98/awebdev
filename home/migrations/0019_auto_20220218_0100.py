# Generated by Django 3.2.10 on 2022-02-17 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20220215_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='c_code',
            name='image',
            field=models.ImageField(upload_to='CCcode'),
        ),
        migrations.AlterField(
            model_name='code_desc',
            name='image',
            field=models.ImageField(upload_to='pycode'),
        ),
    ]
