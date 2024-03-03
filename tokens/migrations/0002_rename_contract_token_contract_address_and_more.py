# Generated by Django 5.0.2 on 2024-03-01 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokens', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='token',
            old_name='contract',
            new_name='contract_address',
        ),
        migrations.AddField(
            model_name='token',
            name='decimals',
            field=models.IntegerField(default=18),
            preserve_default=False,
        ),
    ]
