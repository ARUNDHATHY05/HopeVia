# Generated by Django 5.1.5 on 2025-02-13 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Parent', '0004_alter_tbl_appointment_appointment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_appointment',
            name='appointment_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
