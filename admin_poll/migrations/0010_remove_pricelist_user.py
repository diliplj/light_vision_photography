# Generated by Django 3.1.5 on 2022-01-23 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_poll', '0009_eventimages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pricelist',
            name='user',
        ),
    ]
