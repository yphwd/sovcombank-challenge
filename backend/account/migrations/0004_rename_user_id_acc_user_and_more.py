# Generated by Django 4.1.3 on 2022-11-22 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_rename_user_acc_user_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='acc',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='acc_id',
            new_name='acc',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='user_id',
            new_name='user',
        ),
    ]
