# Generated by Django 3.2.7 on 2021-09-30 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrastion', '0014_alter_stu_data_markshit_12'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stu_data',
            name='markshit_12',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='media/'),
        ),
    ]