# Generated by Django 3.0.9 on 2020-09-10 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebSite', '0003_auto_20200910_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='salecontactus',
            name='centerimg',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='عکس فروشگاه'),
        ),
    ]
