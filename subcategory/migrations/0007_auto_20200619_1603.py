# Generated by Django 3.0.6 on 2020-06-19 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subcategory', '0006_remove_subcategory_catid'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='catid',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='catname',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='subcat',
            field=models.CharField(max_length=20),
        ),
    ]
