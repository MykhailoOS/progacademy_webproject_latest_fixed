# Generated by Django 3.2.23 on 2024-01-20 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furni', '0010_auto_20240118_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourteam',
            name='job',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]