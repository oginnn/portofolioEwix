# Generated by Django 4.2.6 on 2024-01-12 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_reportingresult_image_four_reportingresult_image_one_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportingresult',
            name='video',
            field=models.FileField(null=True, upload_to='videos'),
        ),
    ]
