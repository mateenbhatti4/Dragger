# Generated by Django 3.1.6 on 2022-07-21 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_payments_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bootstrapclasses',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
