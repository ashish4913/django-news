# Generated by Django 3.0.6 on 2020-06-19 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subcategory', '0003_remove_subcategory_catid'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='catid',
            field=models.IntegerField(default=0),
        ),
    ]
