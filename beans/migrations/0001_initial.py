# Generated by Django 3.2.8 on 2021-10-20 18:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TastingNote',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=256, unique=True)),
                ('slug', models.SlugField(default='', max_length=256, null=True)),
            ],
            options={
                'verbose_name': 'Tasting Note',
                'verbose_name_plural': 'Tasting Notes',
            },
        ),
        migrations.CreateModel(
            name='Bean',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=256)),
                ('slug', models.SlugField(default='', max_length=256, null=True)),
                ('roasted_on_date', models.DateField(null=True)),
                ('tasting_notes', models.ManyToManyField(blank=True, to='beans.TastingNote')),
            ],
            options={
                'verbose_name': 'Bean',
                'verbose_name_plural': 'Beans',
            },
        ),
    ]
