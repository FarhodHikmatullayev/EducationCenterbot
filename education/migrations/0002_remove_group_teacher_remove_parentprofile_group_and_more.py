# Generated by Django 5.1.1 on 2024-10-04 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='teacher',
        ),
        migrations.RemoveField(
            model_name='parentprofile',
            name='group',
        ),
        migrations.RemoveField(
            model_name='parentprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='DailyMark',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.DeleteModel(
            name='ParentProfile',
        ),
    ]