# Generated by Django 2.0 on 2022-02-24 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0011_auto_20220224_2227'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cartlist',
            options={'ordering': ['date_added']},
        ),
        migrations.AlterModelTable(
            name='cartlist',
            table='cartlist',
        ),
    ]
