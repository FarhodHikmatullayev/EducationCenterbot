# Generated by Django 5.1.1 on 2024-10-04 10:12

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0003_group_parentprofile_dailymark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailymark',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Izoh'),
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Nomi'),
        ),
        migrations.AlterField(
            model_name='parentprofile',
            name='child_first_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Farzand ismi'),
        ),
        migrations.AlterField(
            model_name='parentprofile',
            name='child_last_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Farzand familiyasi'),
        ),
        migrations.AlterField(
            model_name='teacherprofile',
            name='birth_year',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1970), django.core.validators.MaxValueValidator(2010)], verbose_name="Tug'ilgan yili"),
        ),
        migrations.AlterField(
            model_name='teacherprofile',
            name='experience',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(30)], verbose_name='Ish tajribasi'),
        ),
        migrations.AlterField(
            model_name='teacherprofile',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Ism'),
        ),
        migrations.AlterField(
            model_name='teacherprofile',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Familiya'),
        ),
        migrations.AlterField(
            model_name='teacherprofile',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='education.users', verbose_name='Foydalanuvchi'),
        ),
        migrations.AlterField(
            model_name='users',
            name='full_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='F.I.Sh'),
        ),
        migrations.AlterField(
            model_name='users',
            name='phone',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Telefon raqam'),
        ),
        migrations.AlterField(
            model_name='users',
            name='role',
            field=models.CharField(blank=True, choices=[('admin', 'Admin'), ('user', 'Oddiy foydalanuvchi'), ('teacher', "O'qituvchi"), ('parent', 'Ota-Ona')], default='user', max_length=100, null=True, verbose_name='Foydalanuvchi roli'),
        ),
        migrations.AlterField(
            model_name='users',
            name='telegram_id',
            field=models.BigIntegerField(blank=True, null=True, unique=True, verbose_name='Telegram ID'),
        ),
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Username'),
        ),
    ]
