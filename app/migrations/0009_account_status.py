# Generated by Django 4.0.3 on 2022-03-25 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_rename_accounttype_account_account_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
