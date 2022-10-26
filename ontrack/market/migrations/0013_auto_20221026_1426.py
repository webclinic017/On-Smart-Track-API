# Generated by Django 3.2.16 on 2022-10-26 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0012_auto_20221025_1941'),
    ]

    operations = [
        migrations.CreateModel(
            name='LiveEquityFuture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('prev_close', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('open_price', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('high_price', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('low_price', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('last_price', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('close_price', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('avg_price', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('point_changed', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('percentage_changed', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('expiry_date', models.DateField()),
                ('date', models.DateTimeField()),
                ('pull_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LiveEquityOpenInterest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('lastest_open_interest', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('previous_open_interest', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('change_in_open_interest', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('average_open_interest', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('volume_open_interest', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('future_value', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('option_value', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('underlying_value', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('date', models.DateTimeField()),
                ('pull_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='LiveEquityDerivative',
        ),
        migrations.RemoveField(
            model_name='liveequitydata',
            name='advances',
        ),
        migrations.RemoveField(
            model_name='liveequitydata',
            name='average_open_interest',
        ),
        migrations.RemoveField(
            model_name='liveequitydata',
            name='change_in_open_interest',
        ),
        migrations.RemoveField(
            model_name='liveequitydata',
            name='declines',
        ),
        migrations.RemoveField(
            model_name='liveequitydata',
            name='lastest_open_interest',
        ),
        migrations.RemoveField(
            model_name='liveequitydata',
            name='one_month_ago',
        ),
        migrations.RemoveField(
            model_name='liveequitydata',
            name='one_week_ago',
        ),
        migrations.RemoveField(
            model_name='liveequitydata',
            name='one_year_ago',
        ),
        migrations.RemoveField(
            model_name='liveequitydata',
            name='previous_open_interest',
        ),
        migrations.RemoveField(
            model_name='liveequitydata',
            name='unchanged',
        ),
        migrations.RemoveField(
            model_name='liveequitydata',
            name='underlying_value',
        ),
        migrations.RemoveField(
            model_name='liveequitydata',
            name='volume_open_interest',
        ),
        migrations.RemoveField(
            model_name='liveequityoptionchain',
            name='symbol',
        ),
        migrations.AddField(
            model_name='equity',
            name='industry',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='equity',
            name='isin_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='liveequitydata',
            name='date_month_ago',
            field=models.DateField(blank='True', null=True),
        ),
        migrations.AddField(
            model_name='liveequitydata',
            name='date_year_ago',
            field=models.DateField(blank='True', null=True),
        ),
        migrations.AddField(
            model_name='liveequitydata',
            name='number_of_trades',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True),
        ),
        migrations.AddField(
            model_name='liveequitydata',
            name='price_change_month_ago',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True),
        ),
        migrations.AddField(
            model_name='liveequitydata',
            name='price_change_year_ago',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True),
        ),
        migrations.AddField(
            model_name='liveequitydata',
            name='pull_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='liveequitydata',
            name='quantity_per_trade',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True),
        ),
        migrations.AddField(
            model_name='liveequityoptionchain',
            name='equity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='live_optionchain', to='market.equity'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='liveequityoptionchain',
            name='pull_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='equityderivativeendofday',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='equityendofday',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='indexderivativeendofday',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='indexendofday',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AddField(
            model_name='liveequityopeninterest',
            name='equity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='live_openInterest', to='market.equity'),
        ),
        migrations.AddField(
            model_name='liveequityfuture',
            name='equity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='live_future', to='market.equity'),
        ),
    ]