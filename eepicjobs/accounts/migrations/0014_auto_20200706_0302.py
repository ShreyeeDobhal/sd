# Generated by Django 2.2.2 on 2020-07-06 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20200706_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='tenth_percentage',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='twelth_percentage',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
