# Generated by Django 5.0.1 on 2024-03-21 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SokoApp', '0020_export_delete_exports'),
    ]

    operations = [
        migrations.AlterField(
            model_name='export',
            name='image1',
            field=models.ImageField(null=True, upload_to='exports/'),
        ),
        migrations.AlterField(
            model_name='export',
            name='image2',
            field=models.ImageField(null=True, upload_to='exports/'),
        ),
        migrations.AlterField(
            model_name='export',
            name='image3',
            field=models.ImageField(null=True, upload_to='exports/'),
        ),
    ]
