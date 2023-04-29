# Generated by Django 4.1.6 on 2023-04-29 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0014_alter_complaint_master_updated_at'),
        ('accounts', '0004_remove_customuser_district_remove_customuser_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='complaint_in_district+', to='complaints.district_master', to_field='district_name'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='district_id_no',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='state+', to='complaints.state_master', to_field='state_name'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='state_id_no',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
