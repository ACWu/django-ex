# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-10 14:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_date', models.DateField()),
                ('meals', models.DecimalField(decimal_places=2, max_digits=8)),
                ('hotel', models.DecimalField(decimal_places=2, max_digits=8)),
                ('telephone', models.DecimalField(decimal_places=2, max_digits=8)),
                ('transportation', models.DecimalField(decimal_places=2, max_digits=8)),
                ('miscellaneous', models.DecimalField(decimal_places=2, max_digits=8)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ExpenseReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generate_date', models.DateTimeField(verbose_name='date generated')),
                ('title', models.CharField(max_length=200)),
                ('ending_mileage', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='expenseitem',
            name='expense_report',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expensereport.ExpenseReport'),
        ),
    ]
