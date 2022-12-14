# Generated by Django 3.2.16 on 2022-11-03 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lookup', '0002_alter_setting_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='key_type',
            field=models.CharField(blank=True, choices=[('CONFIGURATION', 'Configuration'), ('EXECUTION_TIME', 'Execution Time')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='key',
            field=models.CharField(choices=[('NO_OF_DAYS_AVG', 'No Of Days Avg'), ('DATAPULL_EQUITY_LOOKUP_PAUSE_HOURS', 'Datapull Equity Lookup Pause Hours'), ('DATAPULL_HOLIDAYS_LOOKUP_PAUSE_HOURS', 'Datapull Holidays Lookup Pause Hours'), ('DATAPULL_EOD_DATA_PAUSE_HOURS', 'Datapull Eod Data Pause Hours'), ('LOOKUP_DATA_OLDER_THAN_DAYS_CAN_BE_DELETED', 'Lookup Data Older Than Days Can Be Deleted'), ('DATAPULL_EQUITY_LOOKUP_LAST_PULL_DATE', 'Datapull Equity Lookup Last Pull Date'), ('DATAPULL_HOLIDAYS_LOOKUP_LAST_PULL_DATE', 'Datapull Holidays Lookup Last Pull Date'), ('DATAPULL_EQUITY_EOD_LAST_PULL_DATE', 'Datapull Equity Eod Last Pull Date'), ('DATAPULL_INDICES_EOD_LAST_PULL_DATE', 'Datapull Indices Eod Last Pull Date')], max_length=50, unique=True),
        ),
    ]
