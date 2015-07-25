# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DService',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('h_datcre', models.DateTimeField(auto_now_add=True, verbose_name=b'Date de creation')),
                ('h_datmod', models.DateTimeField(auto_now=True, verbose_name=b'Date de Modification')),
                ('statut', models.BooleanField(default=True, verbose_name=b'Actif')),
                ('DS_demandeur', models.CharField(max_length=20)),
                ('DS_Sujet', models.CharField(max_length=30)),
                ('DS_Desc', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
