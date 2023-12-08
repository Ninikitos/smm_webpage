# Generated by Django 4.1.7 on 2023-12-08 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0013_alter_coachingpagemodel_coaching_image_one_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientInformationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('company', models.CharField(blank=True, max_length=50)),
                ('scope', models.CharField(blank=True, max_length=100)),
                ('work', models.URLField(blank=True)),
                ('social', models.CharField(blank=True, max_length=50)),
                ('services', models.CharField(blank=True, max_length=400)),
                ('is_social_agency', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('budget', models.IntegerField(blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('message', models.TextField(blank=True, max_length=1200)),
            ],
        ),
    ]