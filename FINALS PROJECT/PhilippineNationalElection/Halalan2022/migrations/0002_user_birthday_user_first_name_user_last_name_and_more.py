# Generated by Django 4.0.4 on 2022-05-17 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Halalan2022', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(),
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='First Name', max_length=300),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='Last Name', max_length=300),
        ),
        migrations.AddField(
            model_name='user',
            name='sex',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
