# Generated by Django 3.2.8 on 2021-10-20 18:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('address_1', models.CharField(max_length=256)),
                ('address_2', models.CharField(max_length=256)),
                ('city', models.CharField(max_length=256)),
                ('state', models.CharField(max_length=256)),
                ('postal_code', models.CharField(max_length=5)),
                ('country', models.CharField(max_length=3)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OperatingHours',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('open_time', models.TimeField()),
                ('close_time', models.TimeField()),
                ('mon_open', models.BooleanField(default=False)),
                ('tue_open', models.BooleanField(default=False)),
                ('wed_open', models.BooleanField(default=False)),
                ('thu_open', models.BooleanField(default=False)),
                ('fri_open', models.BooleanField(default=False)),
                ('sat_open', models.BooleanField(default=False)),
                ('sun_open', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
