# Generated by Django 2.1 on 2018-08-13 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productdesc',
            field=models.CharField(max_length=2000, verbose_name='产品描述'),
        ),
    ]
