# Generated by Django 2.2 on 2020-11-14 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_auto_20201022_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerecord',
            name='service_vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='servicerecords', to='clients.Vehicle'),
        ),
    ]
