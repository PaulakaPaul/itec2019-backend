# Generated by Django 2.1.1 on 2019-11-22 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20191122_2054'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_subcategories',
            new_name='subcategories',
        ),
    ]