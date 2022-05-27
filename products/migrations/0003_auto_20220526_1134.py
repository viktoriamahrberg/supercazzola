# Generated by Django 3.2 on 2022-05-26 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_country'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='img',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='img_url',
            new_name='image_url',
        ),
    ]