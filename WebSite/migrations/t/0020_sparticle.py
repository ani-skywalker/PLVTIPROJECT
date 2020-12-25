# Generated by Django 3.0.9 on 2020-09-18 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebSite', '0019_auto_20200918_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='SPArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SPId', models.CharField(default=0, max_length=200, verbose_name='نام')),
                ('MerchandiseId', models.CharField(default=0, max_length=200, verbose_name='نام')),
                ('Amount', models.CharField(blank=True, default=0, max_length=200, null=True, verbose_name='نام خانوادگی')),
                ('UnitId', models.CharField(default=0, max_length=200, verbose_name='نام')),
                ('UnitPrice', models.CharField(default=0, max_length=200, verbose_name='نام')),
                ('AuxAmount', models.CharField(default=0, max_length=200, verbose_name='نام')),
                ('SPADesc', models.CharField(default=0, max_length=200, verbose_name='نام')),
                ('VTax', models.CharField(default=0, max_length=200, verbose_name='نام')),
                ('VCharge', models.CharField(default=0, max_length=200, verbose_name='نام')),
                ('Percentage', models.CharField(default=0, max_length=200, verbose_name='نام')),
                ('FPId', models.CharField(default=0, max_length=200, verbose_name='نام')),
            ],
            options={
                'verbose_name': 'فاکتور',
                'verbose_name_plural': 'فاکتور ها',
                'db_table': 'SPArticle',
                'permissions': (('can_read_private_section', 'administrator'), ('SubAdmin', 'SubAdmin'), ('user_watcher', 'User')),
            },
        ),
    ]
