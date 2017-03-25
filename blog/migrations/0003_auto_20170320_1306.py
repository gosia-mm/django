# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170320_1305'),
    ]

    operations = [
        migrations.RenameField(
            model_name='status',
            old_name='status_mieszkania',
            new_name='dostepny',
        ),
    ]
