# Generated by Django 3.1.1 on 2020-11-21 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0002_auto_20201111_2200'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='address',
            field=models.CharField(default=None, max_length=100),
        ),
    ]