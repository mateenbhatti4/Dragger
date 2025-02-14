# Generated by Django 4.0.4 on 2022-07-06 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_bootstrapclasses'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=10)),
                ('current_plan', models.CharField(default=None, max_length=50)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
    ]
