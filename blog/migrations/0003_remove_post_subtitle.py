# Generated by Django 2.2.14 on 2020-07-31 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_subtitle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='subtitle',
        ),
    ]