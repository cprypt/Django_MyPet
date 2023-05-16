# Generated by Django 4.2.1 on 2023-05-16 15:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pet', '0004_baseinfo_modify_date_detailinfo_modify_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseinfo',
            name='voter',
            field=models.ManyToManyField(related_name='voter_baseInfo', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='detailinfo',
            name='voter',
            field=models.ManyToManyField(related_name='voter_detailInfo', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='baseinfo',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_baseInfo', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='detailinfo',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_detailInfo', to=settings.AUTH_USER_MODEL),
        ),
    ]
