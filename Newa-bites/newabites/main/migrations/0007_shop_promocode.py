# Generated by Django 5.1.4 on 2024-12-06 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_onlineshop'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='promocode',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
