# Generated by Django 5.1.5 on 2025-02-01 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0017_tbl_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_juvenile',
            name='lawyer',
        ),
        migrations.DeleteModel(
            name='tbl_case',
        ),
        migrations.DeleteModel(
            name='tbl_juvenile',
        ),
    ]
