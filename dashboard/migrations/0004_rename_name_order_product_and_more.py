# Generated by Django 4.0.5 on 2022-07-28 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_order_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='name',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='customer',
            new_name='staff',
        ),
    ]
