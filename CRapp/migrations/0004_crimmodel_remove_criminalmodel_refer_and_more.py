# Generated by Django 4.0.2 on 2022-12-05 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRapp', '0003_auto_20221126_0252'),
    ]

    operations = [
        migrations.CreateModel(
            name='crimModel',
            fields=[
                ('crims_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('height', models.FloatField(blank=True, null=True)),
                ('eyes', models.CharField(max_length=20)),
                ('skin', models.CharField(max_length=20)),
                ('lat1', models.CharField(max_length=20)),
                ('longt1', models.CharField(max_length=20)),
                ('lat2', models.CharField(max_length=20)),
                ('longt2', models.CharField(max_length=20)),
                ('lat3', models.CharField(max_length=20)),
                ('longt3', models.CharField(max_length=20)),
                ('lat4', models.CharField(max_length=20)),
                ('longt4', models.CharField(max_length=20)),
                ('refer', models.ImageField(upload_to='media/')),
            ],
        ),
        migrations.RemoveField(
            model_name='criminalmodel',
            name='refer',
        ),
        migrations.AlterField(
            model_name='criminalmodel',
            name='crim_id',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]