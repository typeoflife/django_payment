# Generated by Django 4.1.1 on 2022-09-25 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_remove_item_price_item_stripe_product_id_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.item'),
        ),
    ]