# Generated by Django 3.1.7 on 2021-03-20 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_tweeprint_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweeprint',
            name='category_slug',
            field=models.SlugField(blank=True, default='', max_length=300, null=True),
        ),
    ]
