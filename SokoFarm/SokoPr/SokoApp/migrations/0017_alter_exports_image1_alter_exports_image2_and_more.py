# Generated by Django 5.0.1 on 2024-03-20 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SokoApp', '0016_alter_offers_image1_alter_offers_image2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exports',
            name='image1',
            field=models.ImageField(upload_to='exports/'),
        ),
        migrations.AlterField(
            model_name='exports',
            name='image2',
            field=models.ImageField(upload_to='exports/'),
        ),
        migrations.AlterField(
            model_name='exports',
            name='image3',
            field=models.ImageField(upload_to='exports/'),
        ),
        migrations.AlterField(
            model_name='offers',
            name='image1',
            field=models.ImageField(null=True, upload_to='offers/'),
        ),
        migrations.AlterField(
            model_name='offers',
            name='image2',
            field=models.ImageField(null=True, upload_to='offers/'),
        ),
        migrations.AlterField(
            model_name='offers',
            name='image3',
            field=models.ImageField(null=True, upload_to='offers/'),
        ),
    ]