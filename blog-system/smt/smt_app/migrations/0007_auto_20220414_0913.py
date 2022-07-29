# Generated by Django 3.2.12 on 2022-04-14 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smt_app', '0006_auto_20220414_0502'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cleaner',
            name='ass_supervisor',
        ),
        migrations.RemoveField(
            model_name='cleaner',
            name='city',
        ),
        migrations.RemoveField(
            model_name='cleaner',
            name='cleaner_group',
        ),
        migrations.RemoveField(
            model_name='cleaner',
            name='user',
        ),
        migrations.RemoveField(
            model_name='cleaner',
            name='zone',
        ),
        migrations.RemoveField(
            model_name='cleaner_group',
            name='supervisor',
        ),
        migrations.RemoveField(
            model_name='cleaner_record',
            name='group',
        ),
        migrations.RemoveField(
            model_name='cleaner_record',
            name='shop_detail',
        ),
        migrations.RemoveField(
            model_name='manager',
            name='city',
        ),
        migrations.RemoveField(
            model_name='manager',
            name='user',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='city',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='history',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='user',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='zone',
        ),
        migrations.RemoveField(
            model_name='shop_detail',
            name='ass_supervisor',
        ),
        migrations.RemoveField(
            model_name='shop_detail',
            name='category',
        ),
        migrations.RemoveField(
            model_name='shop_detail',
            name='city',
        ),
        migrations.RemoveField(
            model_name='shop_detail',
            name='shop_detail',
        ),
        migrations.RemoveField(
            model_name='shop_detail',
            name='shop_owner',
        ),
        migrations.RemoveField(
            model_name='shop_detail',
            name='user',
        ),
        migrations.RemoveField(
            model_name='shop_detail',
            name='zone',
        ),
        migrations.RemoveField(
            model_name='shop_worker',
            name='shop_detail',
        ),
        migrations.RemoveField(
            model_name='supervisor',
            name='city',
        ),
        migrations.RemoveField(
            model_name='supervisor',
            name='manager',
        ),
        migrations.RemoveField(
            model_name='supervisor',
            name='user',
        ),
        migrations.RemoveField(
            model_name='supervisor',
            name='zone',
        ),
        migrations.DeleteModel(
            name='AssistanceSupervisor',
        ),
        migrations.DeleteModel(
            name='Cleaner',
        ),
        migrations.DeleteModel(
            name='Cleaner_Group',
        ),
        migrations.DeleteModel(
            name='Cleaner_Record',
        ),
        migrations.DeleteModel(
            name='Manager',
        ),
        migrations.DeleteModel(
            name='Shop',
        ),
        migrations.DeleteModel(
            name='shop_detail',
        ),
        migrations.DeleteModel(
            name='Shop_Owner',
        ),
        migrations.DeleteModel(
            name='Shop_Worker',
        ),
        migrations.DeleteModel(
            name='Supervisor',
        ),
        migrations.DeleteModel(
            name='tax',
        ),
    ]
