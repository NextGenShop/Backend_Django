# Generated by Django 2.2 on 2021-02-03 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_basket', '0004_auto_20210203_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basketdb',
            name='items',
            field=models.TextField(null=True),
        ),
    ]