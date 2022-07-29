# Generated by Django 3.2.12 on 2022-04-12 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smt_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_category', models.CharField(max_length=20)),
                ('amount', models.IntegerField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='assistancesupervisor',
            name='area',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='assistancesupervisor',
            name='city',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='assistancesupervisor',
            name='zone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='cleaner',
            name='area',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='cleaner',
            name='city',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='cleaner',
            name='working_hours',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='cleaner',
            name='zone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='manager',
            name='city',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='manager',
            name='zone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='shop_manager',
            name='area',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='shop_manager',
            name='city',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='shop_manager',
            name='shop_category',
            field=models.CharField(choices=[('cloth store', 'cloth store'), ('backery', 'backery'), ('electronic shop', 'electronic shop'), ('dry cleaner', 'dry cleaner'), ('general store', 'general store'), ('cafe', 'cafe'), ('tailor', 'tailor'), ('furniture shop', 'furniture shop'), ('software company', 'software company'), ('supermarket', 'supermarket')], default='general store', max_length=20),
        ),
        migrations.AddField(
            model_name='shop_manager',
            name='zone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='shop_owner',
            name='area',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='shop_owner',
            name='city',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='shop_owner',
            name='zone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='supervisor',
            name='area',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='supervisor',
            name='city',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='supervisor',
            name='zone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='roll',
            field=models.CharField(choices=[('MANAGER', 'MANAGER'), ('SUPERVISOR', 'SUPERVISOR'), ('ASSISTANT SUPERVISOR', 'ASSISTANT SUPERVISOR'), ('CLEANER', 'CLEANER'), ('SHOP', 'SHOP'), ('SHOP OWNER', 'SHOP OWNER')], default='MANAGER', max_length=20),
        ),
    ]