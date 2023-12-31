# Generated by Django 4.2.7 on 2023-11-08 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_alter_note_options_alter_user_options_note_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='date_time',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата и время создания'),
        ),
        migrations.AlterField(
            model_name='note',
            name='price',
            field=models.IntegerField(verbose_name='Финансовая стоимость'),
        ),
        migrations.AlterField(
            model_name='note',
            name='reason',
            field=models.CharField(max_length=50, verbose_name='Причина'),
        ),
        migrations.AlterField(
            model_name='note',
            name='sort',
            field=models.IntegerField(choices=[(1, 'Expence'), (2, 'Income')], verbose_name='Вид транзакции'),
        ),
        migrations.AlterField(
            model_name='user',
            name='f_name',
            field=models.CharField(max_length=25, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='l_name',
            field=models.CharField(max_length=25, verbose_name='Фамилия'),
        ),
    ]
