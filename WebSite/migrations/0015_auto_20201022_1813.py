# Generated by Django 3.0.9 on 2020-10-22 14:43

from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('WebSite', '0014_auto_20201021_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='spfactor',
            name='date1',
            field=django_jalali.db.models.jDateField(blank=True, default='1300-01-01', null=True, verbose_name='تاریخ اول'),
        ),
        migrations.AddField(
            model_name='spfactor',
            name='date2',
            field=django_jalali.db.models.jDateField(blank=True, default='1500-01-01', null=True, verbose_name='تاریخ دوم'),
        ),
    ]
