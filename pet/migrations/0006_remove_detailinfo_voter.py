# Generated by Django 4.2.1 on 2023-05-16 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0005_baseinfo_voter_detailinfo_voter_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detailinfo',
            name='voter',
        ),
    ]
