# Generated by Django 2.2.2 on 2021-09-22 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='id',
            field=models.CharField(max_length=15, primary_key=True, serialize=False),
        ),
    ]
