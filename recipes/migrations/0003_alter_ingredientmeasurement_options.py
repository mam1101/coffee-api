# Generated by Django 3.2.8 on 2021-10-20 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_recipe_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredientmeasurement',
            options={'verbose_name': 'Ingredient Measurement', 'verbose_name_plural': 'Ingredient Measurements'},
        ),
    ]
