# Generated by Django 2.0.3 on 2018-09-01 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0021_remove_dressorder_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='dressorder',
            name='sizepk',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
