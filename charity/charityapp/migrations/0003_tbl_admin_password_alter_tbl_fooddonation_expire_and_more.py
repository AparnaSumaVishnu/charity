# Generated by Django 4.2.4 on 2023-10-27 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charityapp', '0002_remove_tbl_receiver_current_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_admin',
            name='password',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='tbl_fooddonation',
            name='expire',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='tbl_fooddonation',
            name='quantity',
            field=models.IntegerField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='tbl_funding',
            name='amount',
            field=models.IntegerField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='tbl_funding',
            name='date',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='tbl_medicinedonation',
            name='quantity',
            field=models.IntegerField(default='', max_length=100),
        ),
    ]