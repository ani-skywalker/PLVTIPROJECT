# Generated by Django 3.0.9 on 2020-09-17 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WebSite', '0016_comment_head'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='brand',
            field=models.ForeignKey(default=1, max_length=200, on_delete=django.db.models.deletion.CASCADE, to='WebSite.productsbrands', verbose_name='نام برند'),
            preserve_default=False,
        ),
    ]
