# Generated by Django 3.2.13 on 2022-05-09 06:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_auto_20220506_0549'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ContactUs',
        ),
        migrations.AlterField(
            model_name='blog',
            name='Date',
            field=models.DateField(default=datetime.date(2022, 5, 9)),
        ),
    ]