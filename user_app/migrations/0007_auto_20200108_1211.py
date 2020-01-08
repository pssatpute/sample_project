# Generated by Django 2.0 on 2020-01-08 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0006_auto_20200108_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(db_column='Is Active', default=True, help_text='Desinates whether this user should be considered active or not.'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(db_column='Is Staff', default=False, help_text='Designates whether this user is a member of staff to access the admin page or not', verbose_name='is_staff'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(db_column='Is Superuser', default=False, help_text='Designates whether this user has all permissions in the admin page or not', verbose_name='is_superuser'),
        ),
    ]
