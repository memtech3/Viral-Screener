# Generated by Django 3.0.4 on 2020-03-25 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ViralScreener', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=200)),
                ('MiddleName', models.CharField(blank=True, max_length=200)),
                ('LastName', models.CharField(max_length=200)),
                ('EmployeeID', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
