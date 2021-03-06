# Generated by Django 3.1.7 on 2021-03-31 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeModel',
            fields=[
                ('idno', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('designation', models.CharField(max_length=30)),
                ('salary', models.FloatField()),
                ('gender', models.CharField(max_length=10)),
                ('contact', models.IntegerField()),
            ],
        ),
    ]
