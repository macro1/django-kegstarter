# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0001_initial'),
        ('beer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keg',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('gallons', models.DecimalField(decimal_places=2, max_digits=4)),
                ('purchase_date', models.DateField(blank=True, null=True)),
                ('beer', models.ForeignKey(to='beer.Beer')),
                ('ledger_entry', models.ForeignKey(help_text="You bought it, there better be a trackable transaction associated with it. Don't include the keg deposit", to='ledger.LedgerEntry')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tap',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('location', models.CharField(max_length=600)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='keg',
            name='tap',
            field=models.ForeignKey(to='keg.Tap'),
            preserve_default=True,
        ),
    ]
