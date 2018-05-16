# Generated by Django 2.0.2 on 2018-05-16 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='old_price',
            field=models.IntegerField(default=0, verbose_name='原价'),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.IntegerField(verbose_name='现价'),
        ),
    ]
