# Generated by Django 3.2.7 on 2021-09-22 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrastion', '0006_alter_stu_data_hobby'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stu_data',
            name='refrance',
        ),
        migrations.AlterField(
            model_name='stu_data',
            name='office_num',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='stu_data',
            name='phone_num',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
