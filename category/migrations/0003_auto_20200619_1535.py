# Generated by Django 3.0.6 on 2020-06-19 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20200619_1533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='catid',
        ),
        migrations.AddField(
            model_name='category',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]