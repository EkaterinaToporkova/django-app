# Generated by Django 4.1.4 on 2022-12-28 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop_menu", "0003_alter_product_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="note",
            field=models.TextField(blank=True, null=True),
        ),
    ]