# Generated by Django 3.2.3 on 2021-12-02 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0004_auto_20211202_0022'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='image_list',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
