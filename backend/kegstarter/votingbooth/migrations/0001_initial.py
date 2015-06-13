# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('keg', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('number_of_votes', models.IntegerField(help_text='How many votes are users allowed for this poll (typically the number of kegs you plan to purchase at once)')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('expected_purchase_date', models.DateField(blank=True, help_text='When you expect to go and buy they kegs', null=True)),
                ('kegs_available', models.ManyToManyField(help_text='Kegs in this poll someone is willing to go and pick up.', to='keg.Keg')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('stars', models.IntegerField(choices=[(1, 'One Star'), (2, 'Two Stars'), (3, 'Three Stars'), (4, 'Four Stars'), (5, 'Five Stars')])),
                ('keg', models.ForeignKey(to='keg.Keg')),
                ('user', models.ForeignKey(help_text='One user, one rating per keg', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('keg', models.ForeignKey(to='keg.Keg')),
                ('poll', models.ForeignKey(to='votingbooth.Poll')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together=set([('keg', 'poll', 'user')]),
        ),
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together=set([('keg', 'user')]),
        ),
    ]
