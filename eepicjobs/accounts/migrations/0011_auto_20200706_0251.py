# Generated by Django 2.2.2 on 2020-07-06 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20200706_0105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='CGPA_For_bachelors',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=2),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='CGPA_For_masters',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=2),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='bachelor_degree',
            field=models.CharField(max_length=255, null=True, verbose_name='Mention Your Bachelor Degree'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='college',
            field=models.CharField(max_length=255, null=True, verbose_name='Mention Your college name'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='hobbies',
            field=models.CharField(max_length=255, null=True, verbose_name='Mention Your Hobbies'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='masters_degree',
            field=models.CharField(max_length=255, null=True, verbose_name='Mention Your Master Degree if any'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='school',
            field=models.CharField(max_length=255, null=True, verbose_name='Mention Your School Name'),
        ),
    ]
