# Generated by Django 4.1.6 on 2023-05-03 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0023_rename_status_id_csr_master_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fir_master',
            name='status',
            field=models.CharField(choices=[('FIR is Filed', 'FIR is Filed'), ('Completed', 'Completed')], default='FIR in progress', max_length=20),
        ),
    ]
