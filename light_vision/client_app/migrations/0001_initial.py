# Generated by Django 3.2.3 on 2021-12-09 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin_app', '0009_photos_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('home_address', models.TextField()),
                ('phone_no', models.IntegerField()),
                ('your_function_from_date', models.DateField()),
                ('your_function_to_date', models.DateField()),
                ('mahal_address', models.TextField()),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.pricelist')),
            ],
        ),
    ]
