# Generated by Django 3.2.5 on 2021-07-19 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0004_remove_blog_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='Img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
