# Generated by Django 3.1 on 2020-08-15 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stackapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='asked_by',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='question',
            name='time',
            field=models.CharField(default='', max_length=250),
        ),
    ]