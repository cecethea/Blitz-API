# Generated by Django 2.0.8 on 2019-02-13 15:48

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0022_coupon_percent'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='couponuser',
            unique_together={('user', 'coupon')},
        ),
    ]
