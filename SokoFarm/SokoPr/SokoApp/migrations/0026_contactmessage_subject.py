# Generated by Django 5.0.3 on 2024-06-01 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SokoApp', '0025_contactmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmessage',
            name='subject',
            field=models.CharField(default='No Subject', max_length=50),
        ),
    ]