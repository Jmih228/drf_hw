# Generated by Django 5.0.6 on 2024-06-06 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_subscription_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='subscription_price',
            field=models.IntegerField(default=500, verbose_name='Цена подписки'),
        ),
    ]