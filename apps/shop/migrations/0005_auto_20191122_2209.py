# Generated by Django 2.1.1 on 2019-11-22 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_shipment_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='optional',
            field=models.TextField(blank=True, max_length=521, null=True),
        ),
    ]
