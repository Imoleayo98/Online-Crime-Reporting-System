# Generated by Django 4.1.6 on 2023-05-04 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0024_alter_fir_master_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='csr_master',
            name='reporting_date_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fir_master',
            name='reporting_date_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]