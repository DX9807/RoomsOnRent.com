# Generated by Django 2.2 on 2019-08-07 10:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('1', 'Andhra Pradesh'), ('2', 'Arunachal Pradesh'), ('3', 'Assam'), ('4', 'Bihar'), ('5', 'Chhattisgarh'), ('6', 'Goa'), ('7', 'Gujarat'), ('8', 'Haryana'), ('9', 'Himachal Pradesh'), ('10', 'Jammu & Kashmir'), ('11', 'Jharkhand'), ('12', 'Karnataka'), ('13', 'Kerala'), ('14', 'Madhya Pradesh'), ('15', 'Maharashtra'), ('16', 'Manipur'), ('17', 'Meghalaya'), ('18', 'Mizoram'), ('19', 'Nagaland'), ('20', 'Odisha'), ('21', 'Punjab'), ('22', 'Rajasthan'), ('23', 'Sikkim'), ('24', 'Tamil Nadu'), ('25', 'Tripura'), ('26', 'Uttarkhand'), ('27', 'Uttar Pradesh'), ('28', 'West Bengal'), ('29', 'Andaman & Nicobar'), ('30', 'Chandigarh'), ('31', 'Dadra & Nagar'), ('32', 'Daman & Diu'), ('33', 'Lakshadweep'), ('34', 'Puducherry'), ('35', 'Delhi')], max_length=256)),
                ('city_area', models.CharField(max_length=256)),
                ('street_address', models.CharField(max_length=300)),
                ('mobile', models.BigIntegerField()),
                ('room_status', models.CharField(max_length=10)),
                ('religious_group', models.CharField(choices=[('1', 'Hinduism'), ('2', 'Islam'), ('3', 'Christianity'), ('4', 'Sikhism'), ('5', 'Jainism'), ('6', 'Budhism'), ('7', 'Zoroastrianism'), ('8', 'Other')], max_length=15)),
                ('monthly_rent', models.PositiveIntegerField()),
                ('desciption', models.CharField(blank=True, max_length=2048)),
                ('ownner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RoomImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_image', models.ImageField(blank=True, upload_to='')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room_service.Room')),
            ],
        ),
    ]
