# Generated by Django 3.2.7 on 2021-09-23 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrastion', '0010_alter_stu_data_joine_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='stu_data',
            name='address',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
