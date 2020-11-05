# Generated by Django 3.1.1 on 2020-11-05 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appV1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmergencyInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relativeName', models.CharField(max_length=100)),
                ('relationship', models.CharField(max_length=20)),
                ('primaryMobileNumber', models.CharField(max_length=10)),
                ('secondaryMobileNumber', models.CharField(max_length=10)),
                ('relativeAddress', models.CharField(max_length=100)),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appV1.personalinfo')),
            ],
        ),
    ]