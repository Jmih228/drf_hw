# Generated by Django 5.0.6 on 2024-06-05 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='price',
            field=models.IntegerField(default=500, verbose_name='Цена'),
        ),
    ]