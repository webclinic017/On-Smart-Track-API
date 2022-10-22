# Generated by Django 3.2.16 on 2022-10-22 12:53

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_cryptography.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('market', '0001_initial'),
        ('lookup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Name of User')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('available_balance', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('ledger_balance', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('credit_limit', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('exclude_from_reports', models.BooleanField(default=False)),
                ('ordinal', models.IntegerField()),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AccountCheque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('cheque_number', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('Date', models.DateTimeField(blank=True, null=True)),
                ('Amount', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('IsBudget', models.TextField()),
                ('is_cancelled', models.TextField()),
                ('is_used', models.TextField()),
                ('is_valid', models.TextField(blank=True, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_cheques', to='users.account')),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AccountStrategies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('capital', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('leverage', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('capital_per_set', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_hedged', models.BooleanField(default=False)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='strategies', to='users.account')),
                ('strategy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_strategies', to='market.markettradingstrategy')),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AccountType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('is_financial', models.BooleanField(default=False)),
                ('icon', models.CharField(blank=True, max_length=200, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('ordinal', models.IntegerField()),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parent_record', to='users.accounttype')),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StrategyTrade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('session', django_cryptography.fields.encrypt(models.CharField(max_length=500))),
                ('initiated_time', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
                ('status', models.CharField(blank=True, choices=[('CREATED', 'Created'), ('OPEN', 'Open'), ('COMPLETE', 'Complete'), ('ACTIVE', 'Active'), ('OPEN PENDING', 'Open Pending'), ('VALIDATION PENDING', 'Validation Pending'), ('PUT ORDER REQ RECEIVED', 'Put Order Req Received'), ('TRIGGER PENDING', 'Trigger Pending'), ('REJECTED', 'Rejected'), ('CANCELLED', 'Cancelled')], max_length=50, null=True)),
                ('symbol', models.CharField(max_length=100)),
                ('symbol_current_market_price', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('exited_time', models.DateTimeField(blank=True, null=True)),
                ('pnl', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('capital', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('account_strategy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trades', to='users.accountstrategies')),
                ('exchange', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trades', to='market.exchange')),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TodoFolder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('folder_name', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='todo_folders', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TodoTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('subject', models.CharField(max_length=50)),
                ('details', models.TextField(blank=True, null=True)),
                ('default_amount', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('priority', models.IntegerField(blank=True, null=True)),
                ('reminder', models.BooleanField(default=False)),
                ('next_due_date', models.DateTimeField(blank=True, null=True)),
                ('folder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='todo_tasks', to='users.todofolder')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='todo_tasks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('mobile', models.CharField(blank=True, max_length=100, null=True)),
                ('address1', models.CharField(blank=True, max_length=200, null=True)),
                ('address2', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=10, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TransactionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('is_expenses', models.BooleanField(null=True)),
                ('is_exclude_from_report', models.BooleanField(default=False)),
                ('icon', models.CharField(blank=True, max_length=200, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('ordinal', models.IntegerField()),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parent_record', to='users.transactiontype')),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TodoTaskFrequency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('frequency', models.CharField(choices=[('DEFAULT', 'Default'), ('DAILY', 'Daily'), ('WEEKLY', 'Weekly'), ('MONTHLY', 'Monthly'), ('QUATERLY', 'Quaterly'), ('HALFYEARLY', 'Halfyearly'), ('YEARLY', 'Yearly')], default='MONTHLY', max_length=50)),
                ('frequency_count', models.IntegerField()),
                ('frequency_start_date', models.DateTimeField()),
                ('frequency_end_date', models.DateTimeField(blank=True, null=True)),
                ('timezone', models.CharField(max_length=100)),
                ('day_of_week', models.CharField(max_length=100)),
                ('day_of_month', models.CharField(max_length=100)),
                ('week_of_month', models.CharField(max_length=100)),
                ('month_of_year', models.CharField(max_length=100)),
                ('occurence_count', models.IntegerField()),
                ('remainder_time', models.TimeField(blank=True, null=True)),
                ('task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='todo_task_frequency', to='users.todotask')),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StrategyTradeOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('order_type', models.CharField(blank=True, choices=[('PRIMARY', 'Primary'), ('STOP_LOSS', 'Stop Loss'), ('TARGET', 'Target')], max_length=50, null=True)),
                ('option_type', models.CharField(blank=True, choices=[('CE', 'Ce'), ('PE', 'Pe')], max_length=50, null=True)),
                ('quantity', models.IntegerField()),
                ('filled_quantity', models.IntegerField()),
                ('pending_quantity', models.IntegerField()),
                ('status', models.CharField(blank=True, choices=[('CREATED', 'Created'), ('OPEN', 'Open'), ('COMPLETE', 'Complete'), ('ACTIVE', 'Active'), ('OPEN PENDING', 'Open Pending'), ('VALIDATION PENDING', 'Validation Pending'), ('PUT ORDER REQ RECEIVED', 'Put Order Req Received'), ('TRIGGER PENDING', 'Trigger Pending'), ('REJECTED', 'Rejected'), ('CANCELLED', 'Cancelled')], max_length=50, null=True)),
                ('institute_order_Id', models.CharField(max_length=50)),
                ('segment', models.CharField(blank=True, choices=[('Equity_Delivery', 'Equity Delivery'), ('Equity_Intraday', 'Equity Intraday'), ('Equity_Futures', 'Equity Futures'), ('Equity_Options', 'Equity Options'), ('CURRENCY', 'Currency'), ('COMMADITY', 'Commadity')], max_length=50, null=True)),
                ('entry_price', models.DecimalField(decimal_places=4, max_digits=18)),
                ('exit_price', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('initial_stoploss_price', models.DecimalField(decimal_places=4, max_digits=18)),
                ('trigger_Price', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('average_Price', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('current_market_price', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('direction', models.CharField(blank=True, choices=[('LONG', 'Long'), ('SHORT', 'Short')], max_length=50, null=True)),
                ('order_validate_type', models.CharField(blank=True, choices=[('MIS', 'Mis'), ('NRML', 'Nrml'), ('CNC', 'Cnc')], max_length=50, null=True)),
                ('order_execute_time', models.DateTimeField()),
                ('order_exit_time', models.DateTimeField(blank=True, null=True)),
                ('last_order_check_time', models.DateTimeField(blank=True, null=True)),
                ('exit_Reason', models.CharField(blank=True, choices=[('SL_HIT', 'Sl Hit'), ('TRAIL_SL_HIT', 'Trail Sl Hit'), ('TARGET_HIT', 'Target Hit'), ('SQUARE_OFF', 'Square Off'), ('SL_CANCELLED', 'Sl Cancelled'), ('TARGET_CANCELLED', 'Target Cancelled')], max_length=50, null=True)),
                ('message_from_instititue', models.CharField(max_length=200)),
                ('brokerage', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('stt', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('transaction_charges', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('gst', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('sebi', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('clearing_charges', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('stamp_duty', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('expiry_date', models.DateTimeField(blank=True, null=True)),
                ('is_weekly_expiry', models.BooleanField(blank=True, null=True)),
                ('option_price', models.IntegerField(blank=True, null=True)),
                ('lot_size', models.IntegerField(blank=True, null=True)),
                ('learning_notes', models.CharField(max_length=200)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_record', to='users.strategytradeorder')),
                ('strategy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='users.strategytrade')),
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
                ('key', models.CharField(choices=[('DEFAULT_THEME', 'Default Theme'), ('DEFAULT_LANGUAGE', 'Default Language'), ('DEFAULT_CURRENCY', 'Default Currency'), ('DEFAULT_DATE_FORMAT', 'Default Date Format'), ('NOTIFICATION_ENABLED', 'Notification Enabled')], max_length=50, unique=True)),
                ('value', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='settings', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='persons', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InterestRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('imterest_rate', models.DecimalField(decimal_places=4, max_digits=18)),
                ('account_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interest_rates', to='users.accounttype')),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DematAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('client_id', models.CharField(max_length=50)),
                ('app_key', django_cryptography.fields.encrypt(models.CharField(max_length=500))),
                ('app_secret', django_cryptography.fields.encrypt(models.CharField(max_length=500))),
                ('Funds', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('available_cash', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('margin', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='demat_account', to='users.account')),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='demat_account', to='market.marketbroker')),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AccountTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('decription', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=4, max_digits=18)),
                ('account_opening_balance', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('account_close_balance', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('principal_amount', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('interest_amount', models.DecimalField(blank=True, decimal_places=4, max_digits=18, null=True)),
                ('occurance_date', models.DateTimeField()),
                ('is_budget', models.BooleanField(default=False)),
                ('is_pursed', models.BooleanField(default=False)),
                ('sequence_number', models.IntegerField(blank=True, null=True)),
                ('previous_transaction_id', models.IntegerField(blank=True, null=True)),
                ('linked_transaction_id', models.IntegerField(blank=True, null=True)),
                ('notes', models.CharField(max_length=100)),
                ('bill_path', models.CharField(max_length=100)),
                ('exclude_from_reports', models.BooleanField(default=False)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='users.account')),
                ('account_cheque', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='users.accountcheque')),
                ('todo_task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.todotask')),
                ('transaction_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='users.transactiontype')),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AccountSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('access_token', django_cryptography.fields.encrypt(models.CharField(max_length=500))),
                ('is_login_initated', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to='users.account')),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AccountInterestRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('imterest_rate', models.DecimalField(decimal_places=4, max_digits=18)),
                ('emi_value', models.DecimalField(decimal_places=4, max_digits=18)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interest_rates', to='users.account')),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='account',
            name='account_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='users.accounttype'),
        ),
        migrations.AddField(
            model_name='account',
            name='currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='lookup.currency'),
        ),
        migrations.AddField(
            model_name='account',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent_record', to='users.account'),
        ),
        migrations.AddField(
            model_name='account',
            name='person',
            field=models.ManyToManyField(related_name='accounts', to='users.Person'),
        ),
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to=settings.AUTH_USER_MODEL),
        ),
    ]
