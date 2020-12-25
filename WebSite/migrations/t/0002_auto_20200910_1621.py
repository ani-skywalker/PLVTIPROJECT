# Generated by Django 3.0.9 on 2020-09-10 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebSite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='centercontactus',
            name='ltworkend',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='ساعت پایان کار در پنج شنبه'),
        ),
        migrations.AlterField(
            model_name='centercontactus',
            name='ltworkstart',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='ساعت شروع کار در پنج شنبه'),
        ),
        migrations.AlterField(
            model_name='centercontactus',
            name='wtworkend',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='ساعت پایان کار در هفته'),
        ),
        migrations.AlterField(
            model_name='centercontactus',
            name='wtworkstart',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='ساعت شروع کار در هفته'),
        ),
        migrations.AlterField(
            model_name='salecontactus',
            name='sltworkend',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='ساعت پایان کار در پنج شنبه'),
        ),
        migrations.AlterField(
            model_name='salecontactus',
            name='sltworkstart',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='ساعت شروع کار در پنج شنبه'),
        ),
        migrations.AlterField(
            model_name='salecontactus',
            name='swtworkend',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='ساعت پایان کار در هفته'),
        ),
        migrations.AlterField(
            model_name='salecontactus',
            name='swtworkstart',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='ساعت شروع کار در هفته'),
        ),
    ]
