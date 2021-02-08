# Generated by Django 2.2 on 2021-02-07 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_basket', '0005_auto_20210203_0950'),
    ]

    operations = [
        migrations.RenameField(
            model_name='basketitem',
            old_name='basketID',
            new_name='shopperID',
        ),
        migrations.RemoveField(
            model_name='basketdb',
            name='shopper',
        ),
        migrations.AddField(
            model_name='basketdb',
            name='shopperID',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
    ]