# Generated by Django 3.0.5 on 2020-06-08 21:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('CID', models.AutoField(primary_key=True, serialize=False)),
                ('ClassID', models.CharField(max_length=2000)),
                ('Name', models.CharField(max_length=2000)),
                ('Subject', models.CharField(max_length=2000)),
                ('Topic', models.CharField(blank=True, max_length=2000, null=True)),
                ('PID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('VID', models.CharField(blank=True, max_length=2000, null=True)),
                ('status', models.CharField(blank=True, max_length=500, null=True)),
                ('CID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Chat')),
                ('PID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Discuss',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('fromPID', models.IntegerField()),
                ('message', models.CharField(max_length=20000)),
                ('time', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('type', models.CharField(default='msg', max_length=100)),
                ('CID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Chat')),
                ('toPID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.UserProfile')),
            ],
        ),
    ]