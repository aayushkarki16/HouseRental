# Generated by Django 3.1.6 on 2021-03-17 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0010_auto_20210317_0035'),
    ]

    operations = [
        migrations.AddField(
            model_name='housedetail',
            name='monthly_price',
            field=models.CharField(default='10000', max_length=200),
        ),
    ]
