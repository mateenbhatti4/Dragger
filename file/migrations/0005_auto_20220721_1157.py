# Generated by Django 3.1.6 on 2022-07-21 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0004_rename_user_id_file_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
