# Generated by Django 4.2.9 on 2024-01-22 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_tweet_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='text',
            field=models.CharField(max_length=280, verbose_name='Text'),
        ),
    ]