# Generated by Django 4.2.4 on 2023-11-01 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charityapp', '0003_tbl_admin_password_alter_tbl_fooddonation_expire_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_fooddonation',
            name='doner_id',
        ),
        migrations.RemoveField(
            model_name='tbl_fooddonation',
            name='receiver_id',
        ),
        migrations.RemoveField(
            model_name='tbl_funding',
            name='doner_id',
        ),
        migrations.RemoveField(
            model_name='tbl_funding',
            name='receiver_id',
        ),
        migrations.RemoveField(
            model_name='tbl_medicinedonation',
            name='doner_id',
        ),
        migrations.RemoveField(
            model_name='tbl_medicinedonation',
            name='receiver_id',
        ),
        migrations.AddField(
            model_name='tbl_fooddonation',
            name='donor_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='charityapp.tbl_donor'),
        ),
        migrations.AddField(
            model_name='tbl_funding',
            name='donor_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='charityapp.tbl_donor'),
        ),
        migrations.AddField(
            model_name='tbl_medicinedonation',
            name='donor_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='charityapp.tbl_donor'),
        ),
        migrations.AddField(
            model_name='tbl_receiver',
            name='donor_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='charityapp.tbl_donor'),
        ),
        migrations.AlterField(
            model_name='tbl_fooddonation',
            name='quantity',
            field=models.CharField(default='', max_length=100),
        ),
    ]
