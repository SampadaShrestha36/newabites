# Generated by Django 5.1.4 on 2024-12-06 12:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_recipe_short_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='OnlineShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('product_url', models.URLField(blank=True, null=True)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='online_shops', to='main.ingredient')),
            ],
        ),
    ]
