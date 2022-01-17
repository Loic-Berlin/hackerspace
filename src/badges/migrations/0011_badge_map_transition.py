# Generated by Django 2.2.24 on 2022-01-10 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('badges', '0010_auto_20200901_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='badge',
            name='map_transition',
            field=models.BooleanField(default=False, help_text='Break maps at this badge.  In maps, this badge will link to a new map that starts with it.'),
        ),
    ]
