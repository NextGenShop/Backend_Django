# Generated by Django 2.2 on 2021-02-03 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_basket', '0002_auto_20210201_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basketitem',
            name='basketItemID',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
