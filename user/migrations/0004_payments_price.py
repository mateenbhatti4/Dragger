# Generated by Django 4.0.4 on 2022-07-06 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_payments'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='price',
            field=models.CharField(blank=True, default=None, max_length=20),
        ),
    ]
