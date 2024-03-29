# Generated by Django 3.2.8 on 2021-10-20 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0002_auto_20211020_1848'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name': 'Address', 'verbose_name_plural': 'Addresses'},
        ),
        migrations.AlterModelOptions(
            name='operatinghours',
            options={'verbose_name': 'Operating Hours', 'verbose_name_plural': 'Operating Hours'},
        ),
        migrations.AddField(
            model_name='distributer',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='address',
            name='address_2',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='cafe',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='roastery',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=256),
        ),
    ]
