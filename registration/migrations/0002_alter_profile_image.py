# Generated by Django 4.2.7 on 2023-11-25 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='media/profile_pics'),
        ),
    ]