# Generated by Django 3.0.6 on 2020-06-19 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subcategory', '0002_auto_20200619_1507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='catid',
        ),
    ]
