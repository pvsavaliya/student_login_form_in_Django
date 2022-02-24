# Generated by Django 3.2.7 on 2021-09-22 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrastion', '0002_alter_stu_data_hobby'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stu_data',
            name='gender',
            field=models.TextField(blank=True, choices=[('M', 'male'), ('F', 'Female')], default=None, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='stu_data',
            name='hobby',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
