# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id_admin', models.AutoField(primary_key=True, serialize=False)),
                ('imie', models.CharField(max_length=50)),
                ('nazwisko', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Klient',
            fields=[
                ('id_klienta', models.AutoField(primary_key=True, serialize=False)),
                ('imie', models.CharField(max_length=50)),
                ('nazwisko', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Miasto',
            fields=[
                ('id_miasta', models.AutoField(primary_key=True, serialize=False)),
                ('nazwa_miasta', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mieszkanie',
            fields=[
                ('id_mieszkania', models.AutoField(primary_key=True, serialize=False)),
                ('ulica', models.CharField(max_length=50)),
                ('nr_mieszkania', models.IntegerField()),
                ('metraz', models.FloatField()),
                ('id_admin', models.ForeignKey(to='blog.Administrator')),
                ('id_miasta', models.ForeignKey(to='blog.Miasto')),
            ],
        ),
        migrations.CreateModel(
            name='Rezerwacja',
            fields=[
                ('id_rezerwacji', models.AutoField(primary_key=True, serialize=False)),
                ('data_od', models.DateTimeField()),
                ('data_do', models.DateTimeField()),
                ('id_klienta', models.ForeignKey(to='blog.Klient')),
                ('id_mieszkania', models.ForeignKey(to='blog.Mieszkanie')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id_statusu', models.AutoField(primary_key=True, serialize=False)),
                ('status_mieszkania', models.BooleanField()),
                ('dostepnosc_od', models.DateTimeField()),
                ('dostepnosc_do', models.DateTimeField()),
                ('id_mieszkania', models.ForeignKey(to='blog.Mieszkanie')),
            ],
        ),
    ]
