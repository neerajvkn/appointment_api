# Generated by Django 3.2.9 on 2021-11-17 00:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_applicant_dw_interviewer_dw'),
    ]

    operations = [
        migrations.DeleteModel(
            name='applicant_dw',
        ),
        migrations.DeleteModel(
            name='interviewer_dw',
        ),
    ]
