# Generated by Django 3.0.8 on 2020-07-30 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20200730_1300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='name',
        ),
        migrations.AddField(
            model_name='item',
            name='num',
            field=models.IntegerField(default=0),
        ),
    ]
