# Generated by Django 5.1.1 on 2024-10-04 07:16

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_remove_group_teacher_remove_parentprofile_group_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nomi')),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='education.teacherprofile', verbose_name="O'qituvchi")),
            ],
            options={
                'verbose_name': 'Group',
                'verbose_name_plural': 'Guruhlar',
                'db_table': 'groups',
            },
        ),
        migrations.CreateModel(
            name='ParentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('child_first_name', models.CharField(max_length=100, verbose_name='Farzand ismi')),
                ('child_last_name', models.CharField(max_length=100, verbose_name='Farzand familiyasi')),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='education.group', verbose_name='Guruhi')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='education.users', verbose_name='Foydalanuvchi')),
            ],
            options={
                'verbose_name': 'Parent',
                'verbose_name_plural': 'Ota-Onalar',
                'db_table': 'parent_profile',
            },
        ),
        migrations.CreateModel(
            name='DailyMark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kategory1', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Kategory 1')),
                ('kategory2', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Kategory 2')),
                ('kategory3', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Kategory 3')),
                ('kategory4', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Kategory 4')),
                ('kategory5', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Kategory 5')),
                ('kategory6', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Kategory 6')),
                ('description', models.TextField(verbose_name='Izoh')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Time')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.parentprofile', verbose_name="O'quvchi")),
            ],
            options={
                'verbose_name': 'Daily Mark',
                'verbose_name_plural': 'Kunlik baholar',
                'db_table': 'daily_mark',
            },
        ),
    ]