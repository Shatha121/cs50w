# Generated by Django 3.2.4 on 2024-08-22 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_alter_auction_listings_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction_listings',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
