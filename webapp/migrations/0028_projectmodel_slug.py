# Generated by Django 4.1.7 on 2023-12-16 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0027_alter_projectmodel_cover_alter_projectmodel_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectmodel',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]