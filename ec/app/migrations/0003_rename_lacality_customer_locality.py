# Generated by Django 5.0.3 on 2024-04-02 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_product_category_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='lacality',
            new_name='locality',
        ),
    ]