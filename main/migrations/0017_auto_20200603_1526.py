# Generated by Django 3.0.6 on 2020-06-03 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_trandingpost_imgname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trandingpost',
            name='img',
            field=models.ImageField(default='', upload_to='news'),
        ),
    ]
