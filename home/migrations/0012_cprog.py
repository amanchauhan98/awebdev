# Generated by Django 3.2.10 on 2022-01-23 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_basicpython'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cprog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('desc', models.TextField()),
                ('image', models.ImageField(upload_to='progC')),
            ],
        ),
    ]