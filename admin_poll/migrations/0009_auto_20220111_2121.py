# Generated by Django 3.1.5 on 2022-01-11 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_poll', '0008_auto_20220111_0017'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageduplicate',
            name='data_from',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='imageduplicate',
            name='data_from_id',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
