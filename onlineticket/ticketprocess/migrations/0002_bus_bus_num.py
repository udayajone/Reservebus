# Generated by Django 4.1.1 on 2022-09-16 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketprocess', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='bus_num',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
