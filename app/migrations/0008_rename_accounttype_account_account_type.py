# Generated by Django 4.0.3 on 2022-03-25 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_rename_idlink_account_id_link_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='accountType',
            new_name='account_type',
        ),
    ]