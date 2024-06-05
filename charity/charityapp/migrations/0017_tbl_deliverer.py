# Generated by Django 4.2.4 on 2023-11-10 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charityapp', '0016_tbl_buyproduct_donor_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_deliverer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('dob', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(default='', max_length=100)),
                ('address', models.CharField(default='', max_length=100)),
                ('phone', models.CharField(default='', max_length=15)),
            ],
        ),
    ]
