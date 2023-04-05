# Generated by Django 4.0.4 on 2022-05-23 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Halalan2022', '0007_position_alter_user_birthday_candidates'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=1000)),
                ('candidate_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Halalan2022.candidates')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Halalan2022.user')),
            ],
        ),
    ]