# Generated by Django 5.0.1 on 2024-03-10 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SokoApp', '0010_alter_category_name_alter_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
