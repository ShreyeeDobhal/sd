# Generated by Django 2.2.2 on 2020-07-03 12:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_jobpost_jobindustry'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='accomplishments',
            field=models.CharField(max_length=255, null=True, verbose_name='accomplishments'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='address',
            field=models.CharField(max_length=255, null=True, verbose_name='address'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='edu',
            field=models.CharField(max_length=255, null=True, verbose_name='Mention Your Education Details'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=254, null=True, validators=[django.core.validators.EmailValidator]),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='experience',
            field=models.CharField(max_length=255, null=True, verbose_name='experience'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='otherLinks',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='prevEmp',
            field=models.CharField(help_text='Mention Your Previous employments', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='projects',
            field=models.CharField(max_length=255, null=True, verbose_name='Give a beief about your projects'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='skills',
            field=models.CharField(help_text='Mention Your Skils', max_length=255, null=True),
        ),
    ]
