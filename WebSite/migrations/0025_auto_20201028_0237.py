# Generated by Django 3.0.9 on 2020-10-27 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebSite', '0024_auto_20201028_0102'),
    ]

    operations = [
        
        migrations.AddField(
            model_name='products',
            name='desc_1',
            field=models.TextField(blank=True, max_length=4000, null=True, verbose_name='توضیحات'),
        ),
        migrations.AddField(
            model_name='products',
            name='desc_2',
            field=models.TextField(blank=True, max_length=4000, null=True, verbose_name='توضیحات'),
        ),
        migrations.AddField(
            model_name='products',
            name='desc_3',
            field=models.TextField(blank=True, max_length=4000, null=True, verbose_name='توضیحات'),
        ),
        migrations.AddField(
            model_name='products',
            name='img_desc_1',
            field=models.ImageField(default='NULL', upload_to='', verbose_name='تصویر توضیح'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='img_desc_2',
            field=models.ImageField(default='NULL', upload_to='', verbose_name='تصویر1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='img_desc_3',
            field=models.ImageField(default='NULL', upload_to='', verbose_name='تصویر1'),
            preserve_default=False,
        ),
    ]
