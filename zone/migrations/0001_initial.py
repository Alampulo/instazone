# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-17 15:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-time'],
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', upload_to='posts/')),
                ('name', models.CharField(max_length=30, null=True)),
                ('location', models.CharField(max_length=60)),
                ('caption', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-time'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=100)),
                ('bio', models.CharField(blank=True, max_length=60)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
        migrations.AddField(
            model_name='images',
            name='user_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comments',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='zone.Images'),
        ),
        migrations.AddField(
            model_name='comments',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]