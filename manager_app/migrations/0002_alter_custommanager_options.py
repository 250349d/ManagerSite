# Generated by Django 5.1.4 on 2024-12-25 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('managerapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='custommanager',
            options={'permissions': [('transaction_detail', 'transaction detail')]},
        ),
    ]
