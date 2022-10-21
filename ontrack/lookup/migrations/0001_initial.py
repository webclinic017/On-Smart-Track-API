# Generated by Django 3.2.16 on 2022-10-21 13:08

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('symbol', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('key', models.CharField(choices=[('NO_OF_DAYS_AVG', 'No Of Days Avg'), ('DATAPULL_EQUITY_LOOKUP_DATE', 'Datapull Equity Lookup Date'), ('DATAPULL_EQUITY_LOOKUP_DAY_PAUSE', 'Datapull Equity Lookup Day Pause'), ('DATAPULL_EQUITY_EOD_DATA_DATE', 'Datapull Equity Eod Data Date'), ('DATAPULL_INDICES_EOD_DATA_DATE', 'Datapull Indices Eod Data Date')], max_length=50, unique=True)),
                ('value', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
            managers=[
                ('datapull_manager', django.db.models.manager.Manager()),
            ],
        ),
    ]
