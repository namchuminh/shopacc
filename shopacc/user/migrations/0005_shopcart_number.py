# Generated by Django 4.0.5 on 2022-07-29 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_remove_shopcart_number_remove_shopcart_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopcart',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]
