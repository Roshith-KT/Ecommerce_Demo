# Generated by Django 4.1.5 on 2023-01-30 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_cartitem_nos'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'ordering': ('date_added',)},
        ),
    ]
