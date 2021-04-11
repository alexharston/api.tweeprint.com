# Generated by Django 3.2 on 2021-04-11 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_tweeprint_tweet_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweeprint',
            name='tweet_author_name',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='tweeprint',
            name='tweet_author_username',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='tweeprint',
            name='tweet_created_at',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]