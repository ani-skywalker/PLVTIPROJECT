# Generated by Django 3.0.9 on 2020-09-18 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebSite', '0021_auto_20200919_0150'),
    ]

    operations = [
        migrations.AddField(
            model_name='sparticle',
            name='Id2',
            field=models.CharField(blank=True, default=0, max_length=200, null=True, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='customers',
            name='Address',
            field=models.CharField(blank=True, default=0, max_length=200, null=True, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='customers',
            name='CSex',
            field=models.CharField(blank=True, default=0, max_length=200, null=True, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='customers',
            name='CellPhone',
            field=models.CharField(blank=True, default=0, max_length=200, null=True, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='customers',
            name='EcCode',
            field=models.CharField(blank=True, default=0, max_length=200, null=True, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='customers',
            name='Email',
            field=models.CharField(blank=True, default=0, max_length=200, null=True, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='customers',
            name='FAccId',
            field=models.CharField(blank=True, default=0, max_length=200, null=True, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='customers',
            name='FPId',
            field=models.CharField(blank=True, default=0, max_length=200, null=True, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='customers',
            name='FaxNo',
            field=models.CharField(blank=True, default=0, max_length=200, null=True, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='customers',
            name='Name',
            field=models.CharField(blank=True, default=0, max_length=200, null=True, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='customers',
            name='PhoneNo',
            field=models.CharField(blank=True, default=0, max_length=200, null=True, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='customers',
            name='SCode',
            field=models.CharField(blank=True, default=0, max_length=200, null=True, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='customers',
            name='TRes',
            field=models.CharField(blank=True, default=0, max_length=200, null=True, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='customers',
            name='UserId',
            field=models.CharField(blank=True, default=0, max_length=200, null=True, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='customers',
            name='ZipCode',
            field=models.CharField(blank=True, default=0, max_length=200, null=True, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='sparticle',
            name='AuxAmount',
            field=models.CharField(blank=True, default=0, max_length=200, null=True, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='sparticle',
            name='FPId',
            field=models.CharField(blank=True, default=0, max_length=200, null=True, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='sparticle',
            name='MerchandiseId',
            field=models.CharField(blank=True, default=0, max_length=200, null=True, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='sparticle',
            name='Percentage',
            field=models.CharField(blank=True, default=0, max_length=200, null=True, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='sparticle',
            name='SPADesc',
            field=models.CharField(blank=True, default=0, max_length=1024, null=True, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='sparticle',
            name='SPId',
            field=models.CharField(blank=True, default=0, max_length=200, null=True, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='sparticle',
            name='UnitId',
            field=models.CharField(blank=True, default=0, max_length=200, null=True, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='sparticle',
            name='UnitPrice',
            field=models.CharField(blank=True, default=0, max_length=200, null=True, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='sparticle',
            name='VCharge',
            field=models.CharField(blank=True, default=0, max_length=200, null=True, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='sparticle',
            name='VTax',
            field=models.CharField(blank=True, default=0, max_length=200, null=True, verbose_name='نام'),
        ),
    ]
