# Generated by Django 3.2.16 on 2022-10-19 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParticipantActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('instrument', models.CharField(choices=[('FUTSTK', 'Futstk'), ('FUTIDX', 'Futidx'), ('OPTSTK', 'Optstk'), ('OPTIDX', 'Optidx'), ('CASH', 'Cash')], max_length=50)),
                ('option_type', models.CharField(blank=True, choices=[('CE', 'Ce'), ('PE', 'Pe')], max_length=50, null=True)),
                ('client_type', models.CharField(choices=[('FII', 'Fii'), ('DII', 'Dii'), ('PRO', 'Pro'), ('RETAIL', 'Retail')], max_length=50)),
                ('buy_amount', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('sell_amount', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('net_amount', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('no_of_contracts', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('open_interest', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('change_from_previous_day', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('is_stats', models.BooleanField(default=False)),
                ('pull_date', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
    ]
