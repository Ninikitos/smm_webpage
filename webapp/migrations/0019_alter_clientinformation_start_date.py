# Generated by Django 4.1.7 on 2023-12-08 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0018_alter_clientinformation_budget_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientinformation',
            name='start_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]