# Generated by Django 5.1.5 on 2025-01-30 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0007_tbl_subcategory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_subcategory',
            old_name='subcat',
            new_name='cat',
        ),
    ]
