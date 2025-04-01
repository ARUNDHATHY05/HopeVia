# Generated by Django 5.1.5 on 2025-02-28 11:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0042_tbl_case'),
        ('RehabilitationStaff', '0004_delete_tbl_rehabilitationreport'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_rehabilitationreport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rehabilitationreport_date', models.DateField(auto_now_add=True)),
                ('rehabilitationreport_details', models.CharField(max_length=200)),
                ('juvenile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_juvenile')),
                ('rehabilitation_staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_rehabilitationstaff')),
            ],
        ),
    ]
