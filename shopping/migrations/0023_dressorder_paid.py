# Generated by Django 2.0.3 on 2018-09-01 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0022_dressorder_sizepk'),
    ]

    operations = [
        migrations.AddField(
            model_name='dressorder',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
