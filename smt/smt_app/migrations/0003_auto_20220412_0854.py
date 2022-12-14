# Generated by Django 3.2.12 on 2022-04-12 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smt_app', '0002_auto_20220412_0637'),
    ]

    operations = [
        migrations.AddField(
            model_name='assistancesupervisor',
            name='manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='smt_app.manager'),
        ),
        migrations.AddField(
            model_name='assistancesupervisor',
            name='supervisor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='smt_app.supervisor'),
        ),
        migrations.AddField(
            model_name='supervisor',
            name='manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='smt_app.manager'),
        ),
    ]
