# Generated by Django 4.1.1 on 2022-12-04 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_alter_price_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='stripe_product_id',
        ),
        migrations.RemoveField(
            model_name='price',
            name='item',
        ),
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='items.price'),
            preserve_default=False,
        ),
    ]
