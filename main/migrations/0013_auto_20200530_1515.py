# Generated by Django 3.0.6 on 2020-05-30 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_trandingpost_writer'),
    ]

    operations = [
        migrations.AddField(
            model_name='trandingpost',
            name='category',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AddField(
            model_name='trandingpost',
            name='catid',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='trandingpost',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
