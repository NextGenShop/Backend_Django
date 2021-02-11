# Generated by Django 2.2 on 2021-02-11 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShopperDB',
            fields=[
                ('shopperId', models.AutoField(primary_key=True, serialize=False)),
                ('shopperEmail', models.EmailField(max_length=254)),
                ('shopperPassword', models.CharField(max_length=128)),
                ('shopperName', models.CharField(max_length=50)),
                ('shopperPhone', models.CharField(max_length=15)),
                ('shopperAddress', models.TextField()),
            ],
        ),
    ]
