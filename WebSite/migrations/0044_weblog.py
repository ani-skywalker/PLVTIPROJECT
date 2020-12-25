# Generated by Django 3.0.9 on 2020-11-17 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebSite', '0043_auto_20201112_1342'),
    ]

    operations = [
        migrations.CreateModel(
            name='weblog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('desc', models.TextField(max_length=4000, verbose_name='شرح')),
                ('img', models.ImageField(blank=True, null=True, upload_to='', verbose_name='عکس ')),
                ('Create_Date', models.DateTimeField(auto_now=True)),
                ('Update_Date', models.DateTimeField(auto_now_add=True)),
                ('Create_Uid', models.IntegerField(blank=True, default=0, null=True, verbose_name='کاربر ایجاد کننده')),
                ('Update_Uid', models.IntegerField(blank=True, default=0, null=True, verbose_name='کاربر ویرایش کننده')),
            ],
            options={
                'verbose_name': 'وبلاگ',
                'verbose_name_plural': 'وبلاگ ها',
                'db_table': 'weblog',
                'ordering': ['id'],
                'permissions': (('can_read_private_section', 'administrator'), ('SubAdmin', 'SubAdmin'), ('user_watcher', 'User')),
            },
        ),
    ]
