# Generated by Django 2.2 on 2019-08-02 06:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import user_auth.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avtar', models.ImageField(blank=True, null=True, upload_to=user_auth.models.upload_avatr)),
                ('mobile', models.BigIntegerField()),
                ('state', models.CharField(max_length=256)),
                ('city', models.CharField(max_length=256)),
                ('locality', models.CharField(max_length=256)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
