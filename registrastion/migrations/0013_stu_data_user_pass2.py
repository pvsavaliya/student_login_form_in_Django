# Generated by Django 3.2.7 on 2021-09-24 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrastion', '0012_rename_address_stu_data_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='stu_data',
            name='user_pass2',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
