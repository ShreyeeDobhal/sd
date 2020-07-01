# Generated by Django 2.2.2 on 2020-06-28 16:50

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200613_1221'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobpost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('JobTitle', models.CharField(max_length=250)),
                ('JobDesciption', models.TextField()),
                ('CompanyName', models.CharField(max_length=250)),
                ('phone_number', models.CharField(max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('email', models.EmailField(max_length=254, null=True, validators=[django.core.validators.EmailValidator])),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('location', models.CharField(max_length=255, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.UserProfile')),
            ],
            options={
                'verbose_name': 'Jobpost',
                'verbose_name_plural': 'Jobposts',
            },
        ),
    ]