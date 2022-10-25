# Generated by Django 3.2.16 on 2022-10-25 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0008_auto_20221025_0814'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participantactivity',
            old_name='change_from_previous_day',
            new_name='change_in_open_interest',
        ),
        migrations.AddField(
            model_name='participantactivity',
            name='date',
            field=models.DateField(),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participantactivity',
            name='value_of_contracts',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True),
        ),
        migrations.AlterField(
            model_name='participantactivity',
            name='pull_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterUniqueTogether(
            name='equityderivativeendofday',
            unique_together={('equity', 'date', 'instrument', 'expiry_date', 'strike_price', 'option_type')},
        ),
        migrations.AlterUniqueTogether(
            name='participantactivity',
            unique_together={('client_type', 'date', 'instrument', 'option_type')},
        ),
        migrations.CreateModel(
            name='ParticipantStatsActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('client_type', models.CharField(choices=[('FII', 'Fii'), ('DII', 'Dii'), ('PRO', 'Pro'), ('RETAIL', 'Retail')], max_length=50)),
                ('instrument', models.CharField(choices=[('FUTSTK', 'Futstk'), ('FUTIDX', 'Futidx'), ('OPTSTK', 'Optstk'), ('OPTIDX', 'Optidx'), ('CASH', 'Cash')], max_length=50)),
                ('no_of_contracts_bought', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('value_of_contracts_bought', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('no_of_contracts_sold', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('value_of_contracts_sold', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('open_interest', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('value_of_open_interest', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('date', models.DateField()),
                ('pull_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
                'unique_together': {('client_type', 'date', 'instrument')},
            },
        ),
        migrations.RemoveField(
            model_name='participantactivity',
            name='is_stats',
        ),
    ]