# Generated by Django 5.1.5 on 2025-02-26 05:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0040_tbl_parent_tbl_juvenile_tbl_case'),
        ('EducationalStaff', '0002_delete_tbl_educationalreport'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_educationalreport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('educationalreport_date', models.DateField(auto_now_add=True)),
                ('educationalreport_details', models.CharField(max_length=200)),
                ('educational_staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_educationalstaff')),
                ('juvenile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_juvenile')),
            ],
        ),
    ]
