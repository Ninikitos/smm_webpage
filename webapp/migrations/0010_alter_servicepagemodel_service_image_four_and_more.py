# Generated by Django 4.1.7 on 2023-11-06 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_coachingpagemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicepagemodel',
            name='service_image_four',
            field=models.ImageField(blank=True, null=True, upload_to='service_page_images/'),
        ),
        migrations.AlterField(
            model_name='servicepagemodel',
            name='service_image_one',
            field=models.ImageField(blank=True, null=True, upload_to='service_page_images/'),
        ),
        migrations.AlterField(
            model_name='servicepagemodel',
            name='service_image_three',
            field=models.ImageField(blank=True, null=True, upload_to='service_page_images/'),
        ),
        migrations.AlterField(
            model_name='servicepagemodel',
            name='service_image_two',
            field=models.ImageField(blank=True, null=True, upload_to='service_page_images/'),
        ),
    ]
