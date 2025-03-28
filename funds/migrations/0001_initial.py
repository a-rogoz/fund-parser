# Generated by Django 5.1.7 on 2025-03-22 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('strategy', models.CharField(choices=[('LSE', 'Long/Short Equity'), ('GM', 'Global Macro'), ('A', 'Arbitrage')], max_length=3, verbose_name='Strategy')),
                ('aum', models.BigIntegerField(blank=True, default=0, verbose_name='Assets Under Management')),
                ('inception_date', models.DateField(blank=True, default='', verbose_name='Inception Date')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
            options={
                'verbose_name': 'Fund',
                'verbose_name_plural': 'Funds',
            },
        ),
    ]
