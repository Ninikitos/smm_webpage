# Generated by Django 4.1.7 on 2023-11-07 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0012_alter_aboutpagemodel_about_image_one_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coachingpagemodel',
            name='coaching_image_one',
            field=models.ImageField(null=True, upload_to='coaching_page_images/'),
        ),
        migrations.AlterField(
            model_name='coachingpagemodel',
            name='coaching_image_two',
            field=models.ImageField(null=True, upload_to='coaching_page_images/'),
        ),
    ]
