# Generated by Django 4.2.7 on 2023-11-18 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(default=None, upload_to='covers/'),
        ),
    ]
