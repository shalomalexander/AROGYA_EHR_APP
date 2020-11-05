# Generated by Django 3.1.1 on 2020-11-05 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appV1', '0007_personalinfo_bloodgroup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emergencyinfo',
            name='secondaryMobileNumber',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='alternateMobileNumber',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='emailId',
            field=models.EmailField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='lastName',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='middleName',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
