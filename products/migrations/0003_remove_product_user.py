# Generated by Django 4.1.5 on 2023-02-22 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='user',
        ),
    ]
