# Generated by Django 4.1.7 on 2023-05-05 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0025_csr_master_reporting_date_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint_master',
            name='info_by_station_incharge',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]