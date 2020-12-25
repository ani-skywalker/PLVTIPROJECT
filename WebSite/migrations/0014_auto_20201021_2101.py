# Generated by Django 3.0.9 on 2020-10-21 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebSite', '0013_auto_20201021_2041'),
    ]

    operations = [
        migrations.CreateModel(
            name='parametrsersal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ersal', models.CharField(max_length=1000, verbose_name='روش ارسال')),
            ],
            options={
                'verbose_name': 'پارامتر',
                'verbose_name_plural': 'پارامتر ها',
                'db_table': 'parametrsersal',
                'ordering': ['id'],
                'permissions': (('can_read_private_section', 'administrator'), ('SubAdmin', 'SubAdmin'), ('user_watcher', 'User')),
            },
        ),
        migrations.CreateModel(
            name='parametrsosool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('osool', models.CharField(max_length=1000, verbose_name='خط مشی')),
                ('Create_Date', models.DateTimeField(auto_now=True)),
                ('Update_Date', models.DateTimeField(auto_now_add=True)),
                ('Create_Uid', models.IntegerField(blank=True, default=0, null=True, verbose_name='کاربر ایجاد کننده')),
                ('Update_Uid', models.IntegerField(blank=True, default=0, null=True, verbose_name='کاربر ویرایش کننده')),
            ],
            options={
                'verbose_name': 'پارامتر',
                'verbose_name_plural': 'پارامتر ها',
                'db_table': 'parametrsosool',
                'ordering': ['id'],
                'permissions': (('can_read_private_section', 'administrator'), ('SubAdmin', 'SubAdmin'), ('user_watcher', 'User')),
            },
        ),
    ]
