# Generated by Django 2.2 on 2019-08-08 10:49

from django.db import migrations, models
import room_service.models


class Migration(migrations.Migration):

    dependencies = [
        ('room_service', '0005_auto_20190808_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='cover_image',
            field=models.ImageField(default=None, upload_to=room_service.models.upload_cover_image),
            preserve_default=False,
        ),
    ]
