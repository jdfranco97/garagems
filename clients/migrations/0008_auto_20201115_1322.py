# Generated by Django 2.2 on 2020-11-15 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0007_auto_20201115_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerecord',
            name='service_date',
            field=models.DateField(blank=True, null=True, verbose_name='Date'),
        ),
    ]
