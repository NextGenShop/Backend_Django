# Generated by Django 2.2 on 2021-02-17 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_basket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basketitem',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
