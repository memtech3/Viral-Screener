# Generated by Django 3.0.4 on 2020-03-23 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlertMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('color', models.CharField(choices=[('success', 'green'), ('primary', 'blue'), ('warning', 'yellow'), ('danger', 'red')], max_length=200)),
                ('content', models.TextField()),
                ('dismissable', models.BooleanField()),
            ],
        ),
    ]
