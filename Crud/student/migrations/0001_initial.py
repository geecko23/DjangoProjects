# Generated by Django 5.2.3 on 2025-06-22 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.PositiveIntegerField()),
                ('branch', models.CharField(choices=[('CE', 'CE'), ('EXTC', 'EXTC'), ('ME', 'ME'), ('IT', 'IT')], max_length=20)),
            ],
        ),
    ]
