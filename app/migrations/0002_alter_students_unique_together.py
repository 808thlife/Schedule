# Generated by Django 4.1.4 on 2023-03-09 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='students',
            unique_together={('group_year', 'group_title', 'group_number')},
        ),
    ]