# Generated by Django 5.1.5 on 2025-01-30 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0008_rename_subcat_tbl_subcategory_cat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_subcategory',
            old_name='cat',
            new_name='category_id',
        ),
    ]
