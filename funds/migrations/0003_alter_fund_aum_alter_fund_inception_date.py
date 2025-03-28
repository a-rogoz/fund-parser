# Generated by Django 5.1.7 on 2025-03-23 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funds', '0002_alter_fund_strategy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fund',
            name='aum',
            field=models.BigIntegerField(blank=True, default=None, null=True, verbose_name='Assets Under Management'),
        ),
        migrations.AlterField(
            model_name='fund',
            name='inception_date',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Inception Date'),
        ),
    ]
