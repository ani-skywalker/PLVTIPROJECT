# Generated by Django 3.0.9 on 2020-10-24 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebSite', '0016_auto_20201024_0601'),
    ]

    operations = [
      
        migrations.AddField(
            model_name='sellbascket',
            name='TrackingCode',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='کد رهگیری'),
        ),
    ]
