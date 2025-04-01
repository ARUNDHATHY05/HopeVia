# Generated by Django 5.1.5 on 2025-02-26 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0038_delete_tbl_fees'),
        ('EducationalStaff', '0002_delete_tbl_educationalreport'),
        ('HealthStaff', '0002_delete_tbl_healthreport'),
        ('Lawyer', '0005_delete_tbl_hearing'),
        ('Parent', '0008_remove_tbl_complaint_parent_delete_tbl_appointment_and_more'),
        ('RehabilitationStaff', '0002_delete_tbl_rehabilitationreport'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_juvenile',
            name='lawyer',
        ),
        migrations.RemoveField(
            model_name='tbl_juvenile',
            name='parent',
        ),
        migrations.DeleteModel(
            name='tbl_case',
        ),
        migrations.DeleteModel(
            name='tbl_juvenile',
        ),
        migrations.DeleteModel(
            name='tbl_parent',
        ),
    ]
