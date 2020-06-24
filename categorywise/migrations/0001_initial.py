# Generated by Django 3.0.6 on 2020-06-19 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=100)),
                ('pub_date', models.DateField()),
                ('img', models.ImageField(default='', upload_to='news')),
                ('imgname', models.CharField(default='-', max_length=50)),
                ('details', models.TextField(default='-', max_length=500000)),
                ('writer', models.CharField(default='Ashish', max_length=50)),
                ('views', models.IntegerField(default=0)),
                ('cat', models.CharField(max_length=50)),
                ('subcat', models.CharField(max_length=50)),
                ('catid', models.IntegerField()),
            ],
        ),
    ]