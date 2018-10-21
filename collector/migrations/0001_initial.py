# Generated by Django 2.1.2 on 2018-10-12 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.FloatField()),
                ('timedate', models.DateTimeField(auto_now_add=True)),
                ('action', models.CharField(choices=[(0, 'changed relay to 0'), (1, 'changed relay to 1')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('val_key', models.CharField(max_length=128, unique=True)),
                ('value', models.CharField(max_length=4096, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Temps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.FloatField()),
                ('timedate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]