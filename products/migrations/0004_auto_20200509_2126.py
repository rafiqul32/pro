# Generated by Django 3.0.5 on 2020-05-09 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200508_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]
