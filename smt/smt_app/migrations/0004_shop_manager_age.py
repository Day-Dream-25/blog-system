# Generated by Django 3.2.12 on 2022-04-12 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smt_app', '0003_auto_20220412_0854'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop_manager',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]
