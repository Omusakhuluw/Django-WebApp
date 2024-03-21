# Generated by Django 5.0.1 on 2024-03-20 22:03

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SokoApp', '0019_rename_offers_offer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Export',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('image1', models.ImageField(upload_to='exports/')),
                ('image2', models.ImageField(upload_to='exports/')),
                ('image3', models.ImageField(upload_to='exports/')),
                ('subcategory', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=15)),
                ('quantity', models.CharField(max_length=20)),
                ('ready_for_purchase', models.BooleanField()),
                ('purchase_timeframe', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('contacts', models.CharField(max_length=15)),
                ('additional_info', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exports', to='SokoApp.category')),
            ],
        ),
        migrations.DeleteModel(
            name='Exports',
        ),
    ]
