# Generated by Django 4.1.6 on 2023-05-01 10:06

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0015_alter_complaint_master_status_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='csr_master',
            fields=[
                ('csr_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('csr_no', models.CharField(max_length=150, unique=True)),
                ('complainant_name', models.CharField(max_length=150)),
                ('complainant_gender', models.CharField(max_length=6)),
                ('complainant_contact_no', models.IntegerField()),
                ('complainant_email', models.EmailField(max_length=254, verbose_name='Email Address')),
                ('complainant_dob', models.DateField()),
                ('complainant_address', models.TextField()),
                ('complainant_state_id', models.IntegerField(blank=True, null=True)),
                ('complainant_district_id', models.IntegerField(blank=True, null=True)),
                ('complainant_pin_code', models.IntegerField()),
                ('state_id', models.IntegerField(blank=True, null=True)),
                ('district_id', models.IntegerField(blank=True, null=True)),
                ('station_id', models.IntegerField(blank=True, null=True)),
                ('status_id', models.CharField(choices=[('CSR in progress', 'CSR in progress'), ('Completed', 'Completed')], default='CSR in progress', max_length=20)),
                ('other_crime_category', models.CharField(blank=True, max_length=150, null=True)),
                ('subject', models.CharField(max_length=150)),
                ('detailed_description', models.TextField(max_length=10000)),
                ('delay_reason', models.TextField(blank=True, max_length=1000, null=True)),
                ('datetime_of_occurence', models.DateTimeField()),
                ('place_of_occurence', models.CharField(blank=True, max_length=150, null=True)),
                ('evidence_image', models.ImageField(blank=True, null=True, upload_to='complaint images/')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('complainant_district_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="complainant's_district+", to='complaints.district_master', to_field='district_name')),
                ('complainant_state_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="complainant's_state+", to='complaints.state_master', to_field='state_name')),
                ('crime_category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='complaints.crime_category_master', to_field='crime_category_name')),
                ('district_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='complaint_in_district+', to='complaints.district_master', to_field='district_name')),
                ('state_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='complaint_in_state+', to='complaints.state_master', to_field='state_name')),
                ('station_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='complainant_in_police_station+', to='complaints.police_station_master', to_field='station_name')),
            ],
            options={
                'verbose_name_plural': 'CSRs',
            },
        ),
    ]
