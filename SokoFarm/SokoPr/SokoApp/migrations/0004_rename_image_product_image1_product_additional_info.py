# Generated by Django 5.0.1 on 2024-03-03 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SokoApp', '0003_alter_product_category_alter_product_subcategory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='product',
            name='additional_info',
            field=models.TextField(default=''),
        ),
    ]
