# Generated by Django 3.2.5 on 2021-07-19 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='Img',
        ),
    ]
