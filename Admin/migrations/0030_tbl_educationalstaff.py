# Generated by Django 5.1.5 on 2025-02-05 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0029_tbl_rehabilitationreport'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_educationalstaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('educationalstaff_name', models.CharField(max_length=30)),
                ('educationalstaff_email', models.EmailField(max_length=254)),
                ('educationalstaff_contact', models.CharField(max_length=11)),
                ('educationalstaff_password', models.CharField(max_length=30)),
            ],
        ),
    ]
