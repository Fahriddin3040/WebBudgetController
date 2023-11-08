# Generated by Django 4.2.7 on 2023-11-07 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='web.users'),
        ),
        migrations.AlterField(
            model_name='notes',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='notes',
            name='reason',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='notes',
            name='sort',
            field=models.IntegerField(choices=[(1, 'Expence'), (2, 'Income')], default=1),
        ),
    ]