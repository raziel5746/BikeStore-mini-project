# Generated by Django 3.0.1 on 2019-12-25 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0002_auto_20191224_1436'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rental',
            old_name='customer',
            new_name='customer_id',
        ),
        migrations.RenameField(
            model_name='rental',
            old_name='vehicle',
            new_name='vehicle_id',
        ),
    ]
