# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='category',
            field=models.CharField(choices=[('CH', 'Character'), ('FA', 'Faction'), ('EV', 'Event'), ('TC', 'Technology'), ('LC', 'Location'), ('MS', 'Miscellaneous')], max_length=2, default='MS'),
            preserve_default=True,
        ),
    ]
