# Generated by Django 4.1.6 on 2023-05-01 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0015_alter_complaint_master_status_id_and_more'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('accounts', '0024_police'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='police',
            new_name='police_officer',
        ),
    ]