# Generated by Django 4.2.4 on 2023-11-02 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charityapp', '0006_tbl_fooddonation_otherfoodname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_fooddonation',
            name='otherfoodname',
        ),
    ]