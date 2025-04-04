# Generated by Django 5.1.5 on 2025-01-30 11:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0012_tbl_juvenile'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_name', models.CharField(max_length=30)),
                ('case_details', models.CharField(max_length=100)),
                ('case_date', models.DateField()),
                ('casetype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_casetype')),
                ('juvenile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_juvenile')),
                ('lawyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_lawyer')),
            ],
        ),
    ]
