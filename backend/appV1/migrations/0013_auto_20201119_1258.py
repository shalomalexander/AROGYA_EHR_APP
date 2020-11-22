# Generated by Django 3.0.8 on 2020-11-19 07:28

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appV1', '0012_bloodpressure'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodpressure',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.CreateModel(
            name='BodyTemperature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.IntegerField()),
                ('date', models.DateField(default=datetime.date.today)),
                ('notes', models.CharField(max_length=255, null=True)),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appV1.PersonalInfo')),
            ],
        ),
    ]
