# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-09 21:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name_plural': 'Activities',
            },
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(max_length=128)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Activity')),
            ],
            options={
                'verbose_name_plural': 'Jobs',
            },
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perform', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name_plural': 'Performances',
            },
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('performance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Performance')),
            ],
            options={
                'verbose_name_plural': 'Personals',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name_plural': 'Positions',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(default='', max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=15)),
                ('description', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Statuss',
            },
        ),
        migrations.AddField(
            model_name='personal',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Position'),
        ),
        migrations.AddField(
            model_name='jobs',
            name='personal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Personal'),
        ),
        migrations.AddField(
            model_name='jobs',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Project'),
        ),
        migrations.AddField(
            model_name='jobs',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Status'),
        ),
    ]
