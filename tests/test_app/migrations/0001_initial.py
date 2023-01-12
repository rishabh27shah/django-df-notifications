# Generated by Django 4.1.5 on 2023-01-12 11:03

import df_notifications.fields
import df_notifications.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('df_notifications', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostNotificationRule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel', df_notifications.fields.NoMigrationsChoicesField(max_length=255)),
                ('template_prefix', models.CharField(max_length=255)),
                ('context', models.JSONField(blank=True, default=dict)),
                ('is_published_prev', models.BooleanField(default=False)),
                ('is_published_next', models.BooleanField(default=True)),
                ('history', models.ManyToManyField(blank=True, to='df_notifications.notificationhistory')),
            ],
            options={
                'abstract': False,
            },
            bases=(df_notifications.models.GenericBase, models.Model),
        ),
        migrations.CreateModel(
            name='PostNotificationReminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel', df_notifications.fields.NoMigrationsChoicesField(max_length=255)),
                ('template_prefix', models.CharField(max_length=255)),
                ('context', models.JSONField(blank=True, default=dict)),
                ('history', models.ManyToManyField(blank=True, to='df_notifications.notificationhistory')),
            ],
            options={
                'abstract': False,
            },
            bases=(df_notifications.models.GenericBase, models.Model),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
