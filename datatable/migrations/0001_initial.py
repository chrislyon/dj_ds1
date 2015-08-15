# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Serveur',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('h_datcre', models.DateTimeField(auto_now_add=True, verbose_name=b'Date de creation')),
                ('h_datmod', models.DateTimeField(auto_now=True, verbose_name=b'Date de Modification')),
                ('statut', models.BooleanField(default=True, verbose_name=b'Actif')),
                ('In_Nom', models.CharField(max_length=30, verbose_name=b'Nom')),
                ('In_Type', models.CharField(default=b'VM', max_length=3, verbose_name=b'Type', choices=[(b'VM', b'Machine Virtuelle'), (b'PHY', b'Physique')])),
                ('In_IP', models.GenericIPAddressField(default=b'127.0.0.1', verbose_name=b'Adr IP')),
                ('In_OSTYPE', models.CharField(default=b'UNIX', max_length=5, verbose_name=b'Famille OS', choices=[(b'UNIX', b'UNIX'), (b'WIN', b'WINDOWS'), (b'AUT', b'AUTRES')])),
                ('In_OSVersion', models.CharField(max_length=30, verbose_name=b'OS Version', blank=True)),
                ('In_Desc', models.TextField(default=b' ', verbose_name=b'Description', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
