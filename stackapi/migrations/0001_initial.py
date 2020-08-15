# Generated by Django 3.1 on 2020-08-15 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=300)),
                ('vote_count', models.IntegerField(default=0)),
                ('views', models.CharField(max_length=50)),
                ('tags', models.CharField(max_length=250)),
            ],
        ),
    ]