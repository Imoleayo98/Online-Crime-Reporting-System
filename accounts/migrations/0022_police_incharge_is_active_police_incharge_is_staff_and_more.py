# Generated by Django 4.1.6 on 2023-04-30 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_alter_police_incharge_incharge_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='police_incharge',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='police_incharge',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='police_incharge',
            name='is_user',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='police_incharge',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='police_incharge',
            name='profile_image',
            field=models.ImageField(blank=True, default='Profile images/default.png', null=True, upload_to='Profile images/'),
        ),
    ]