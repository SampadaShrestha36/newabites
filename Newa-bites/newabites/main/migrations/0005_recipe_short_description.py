# Generated by Django 5.1.4 on 2024-12-06 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_recipe_image1_recipe_image2_recipe_image3'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='short_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
