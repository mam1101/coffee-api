# Generated by Django 3.2.8 on 2021-10-20 18:48

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0001_initial'),
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
        migrations.AlterField(
            model_name='cafe',
            name='full_address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shops.address'),
        ),
        migrations.AlterField(
            model_name='cafe',
            name='operating_hours',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shops.operatinghours'),
        ),
        migrations.AlterField(
            model_name='distributer',
            name='full_address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shops.address'),
        ),
        migrations.AlterField(
            model_name='distributer',
            name='operating_hours',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shops.operatinghours'),
        ),
        migrations.AlterField(
            model_name='roastery',
            name='full_address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shops.address'),
        ),
        migrations.AlterField(
            model_name='roastery',
            name='operating_hours',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shops.operatinghours'),
        ),
    ]
