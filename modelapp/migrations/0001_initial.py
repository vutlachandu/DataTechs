# Generated by Django 3.1.3 on 2020-12-08 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=30)),
                ('tname', models.CharField(max_length=30)),
                ('sdate', models.CharField(max_length=30)),
                ('duration', models.CharField(max_length=30)),
            ],
        ),
    ]
