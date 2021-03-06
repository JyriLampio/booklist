# Generated by Django 3.2 on 2022-05-27 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_rename_customer_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='edition',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]
