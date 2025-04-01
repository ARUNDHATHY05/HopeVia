# Generated by Django 5.1.5 on 2025-02-01 09:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0021_remove_tbl_juvenile_lawyer_delete_tbl_case_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_juvenile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('juvenile_name', models.CharField(max_length=30)),
                ('juvenile_age', models.CharField(max_length=2)),
                ('juvenile_gender', models.CharField(max_length=10)),
                ('juvenile_height', models.CharField(max_length=10)),
                ('juvenile_weight', models.CharField(max_length=10)),
                ('juvenile_address', models.CharField(max_length=100)),
                ('juvenile_photo', models.FileField(upload_to='Assets/Admin/Photo')),
                ('juvenile_proof', models.FileField(upload_to='Assets/Admin/Proof')),
                ('lawyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_lawyer')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_parent')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_name', models.CharField(max_length=30)),
                ('case_details', models.CharField(max_length=100)),
                ('case_date', models.DateField()),
                ('casetype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_casetype')),
                ('lawyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_lawyer')),
                ('juvenile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_juvenile')),
            ],
        ),
    ]
