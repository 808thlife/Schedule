# Generated by Django 4.1.5 on 2023-03-08 16:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Write Description of this class (Who is the teacher? Who teacher going to teach and what subject etc...)', max_length=32)),
                ('time', models.CharField(max_length=12)),
                ('cabinet', models.IntegerField()),
                ('description', models.CharField(max_length=100, null=True)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_year', models.IntegerField()),
                ('group_title', models.CharField(max_length=10)),
                ('group_number', models.IntegerField()),
                ('lessons', models.ManyToManyField(to='app.lesson')),
            ],
        ),
    ]
