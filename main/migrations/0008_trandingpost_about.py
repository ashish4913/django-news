# Generated by Django 3.0.6 on 2020-05-18 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200518_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='trandingpost',
            name='about',
            field=models.CharField(default='-', max_length=10),
            preserve_default=False,
        ),
    ]
