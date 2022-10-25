# Generated by Django 3.2.16 on 2022-10-25 01:52

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0006_auto_20221023_1729'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='equityderivativeendofday',
            managers=[
                ('backend', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='indexderivativeendofday',
            managers=[
                ('backend', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RemoveField(
            model_name='indexderivativeendofday',
            name='change_in_open_interest',
        ),
        migrations.RemoveField(
            model_name='indexderivativeendofday',
            name='close_price',
        ),
        migrations.RemoveField(
            model_name='indexderivativeendofday',
            name='expiry_date',
        ),
        migrations.RemoveField(
            model_name='indexderivativeendofday',
            name='high_price',
        ),
        migrations.RemoveField(
            model_name='indexderivativeendofday',
            name='instrument',
        ),
        migrations.RemoveField(
            model_name='indexderivativeendofday',
            name='low_price',
        ),
        migrations.RemoveField(
            model_name='indexderivativeendofday',
            name='no_of_contracts',
        ),
        migrations.RemoveField(
            model_name='indexderivativeendofday',
            name='open_interest',
        ),
        migrations.RemoveField(
            model_name='indexderivativeendofday',
            name='open_price',
        ),
        migrations.RemoveField(
            model_name='indexderivativeendofday',
            name='option_type',
        ),
        migrations.RemoveField(
            model_name='indexderivativeendofday',
            name='pull_date',
        ),
        migrations.RemoveField(
            model_name='indexderivativeendofday',
            name='settle_price',
        ),
        migrations.RemoveField(
            model_name='indexderivativeendofday',
            name='strike_price',
        ),
        migrations.RemoveField(
            model_name='indexderivativeendofday',
            name='value_of_contracts',
        ),
        migrations.RemoveField(
            model_name='liveequitydata',
            name='symbol',
        ),
        migrations.AddField(
            model_name='equityderivativeendofday',
            name='date',
            field=models.DateField(),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='equityderivativeendofday',
            name='pull_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterUniqueTogether(
            name='equityderivativeendofday',
            unique_together={('equity', 'instrument', 'expiry_date', 'strike_price', 'option_type')},
        ),
    ]