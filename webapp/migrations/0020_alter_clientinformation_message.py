# Generated by Django 4.1.7 on 2023-12-08 13:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0019_alter_clientinformation_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientinformation',
            name='message',
            field=models.TextField(blank=True, default=django.utils.timezone.now, max_length=1200),
        ),
    ]
