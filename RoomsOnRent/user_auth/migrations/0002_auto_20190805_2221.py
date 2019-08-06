# Generated by Django 2.2 on 2019-08-05 16:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='state',
            field=models.CharField(choices=[('1', 'Andhra Pradesh'), ('2', 'Arunachal Pradesh'), ('3', 'Assam'), ('4', 'Bihar'), ('5', 'Chhattisgarh'), ('6', 'Goa'), ('7', 'Gujarat'), ('8', 'Haryana'), ('9', 'Himachal Pradesh'), ('10', 'Jammu & Kashmir'), ('11', 'Jharkhand'), ('12', 'Karnataka'), ('13', 'Kerala'), ('14', 'Madhya Pradesh'), ('15', 'Maharashtra'), ('16', 'Manipur'), ('17', 'Meghalaya'), ('18', 'Mizoram'), ('19', 'Nagaland'), ('20', 'Odisha'), ('21', 'Punjab'), ('22', 'Rajasthan'), ('23', 'Sikkim'), ('24', 'Tamil Nadu'), ('25', 'Tripura'), ('26', 'Uttarkhand'), ('27', 'Uttar Pradesh'), ('28', 'West Bengal'), ('29', 'Andaman & Nicobar'), ('30', 'Chandigarh'), ('31', 'Dadra & Nagar'), ('32', 'Daman & Diu'), ('33', 'Lakshadweep'), ('34', 'Puducherry'), ('35', 'Delhi')], max_length=256),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userprofile', to=settings.AUTH_USER_MODEL),
        ),
    ]