# Generated by Django 3.2 on 2022-05-27 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20220527_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]