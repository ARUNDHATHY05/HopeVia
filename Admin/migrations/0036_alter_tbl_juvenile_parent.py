# Generated by Django 5.1.5 on 2025-02-13 10:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0035_delete_tbl_rehabilitationreport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_juvenile',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_parent'),
        ),
    ]
