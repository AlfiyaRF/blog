# Generated by Django 2.2.14 on 2020-07-31 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subtitle',
            field=models.CharField(default=0, max_length=500),
            preserve_default=False,
        ),
    ]
