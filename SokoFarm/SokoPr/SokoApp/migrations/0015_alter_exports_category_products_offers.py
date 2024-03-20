# Generated by Django 5.0.1 on 2024-03-18 20:49

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SokoApp', '0014_alter_order_price_range_alter_order_quantity_exports'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exports',
            name='category_products',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='export_category_products', to='SokoApp.product'),
        ),
        migrations.CreateModel(
            name='Offers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('initial_price', models.CharField(max_length=20)),
                ('current_price', models.CharField(max_length=20)),
                ('image1', models.ImageField(upload_to='products/')),
                ('image2', models.ImageField(upload_to='products/')),
                ('image3', models.ImageField(upload_to='products/')),
                ('subcategory', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('quantity', models.CharField(max_length=20)),
                ('purchase_timeframe', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('contacts', models.CharField(max_length=15)),
                ('additional_info', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offers', to='SokoApp.category')),
                ('category_products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_products', to='SokoApp.product')),
            ],
        ),
    ]
