# Generated by Django 4.1.4 on 2024-03-12 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charityapp', '0025_tbl_deliverer_receiver_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_deliverer',
            name='receiver_id',
        ),
    ]
