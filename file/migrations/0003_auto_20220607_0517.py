# Generated by Django 3.2.6 on 2022-06-07 05:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('file', '0002_file_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='isProfile',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='file',
            name='user_id',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
