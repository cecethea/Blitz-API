# Generated by Django 2.0.8 on 2019-01-23 16:11

from django.contrib.contenttypes.models import ContentType
from django.db import migrations, models
from django.db.models import Q
import django.db.models.deletion


def move_coupon_to_orderlines(apps, schema_editor):
    '''
    We can't import the Order model directly as it may be a newer
    version than this migration expects. We use the historical version.
    '''
    Order = apps.get_model('store', 'Order')
    Retirement = apps.get_model('retirement', 'Retirement')
    for order in Order.objects.all():
        orderlines = order.order_lines.filter(
            models.Q(content_type__model='membership') |
            models.Q(content_type__model='package') |
            models.Q(content_type__model='retirement')
        )
        no_price_orderline = order.order_lines.exclude(
            models.Q(content_type__model='membership') |
            models.Q(content_type__model='package') |
            models.Q(content_type__model='retirement')
        )
        for orderline in orderlines:
            orderline.coupon = None
            orderline.coupon_real_value = 0
            ct = ContentType.objects.get(
                model=orderline.content_type.model,
                app_label=orderline.content_type.app_label
            )
            content_object = ct.get_object_for_this_type(pk=orderline.object_id)
            orderline.cost = content_object.price * orderline.quantity
            orderline.save()

        for orderline in no_price_orderline:
            orderline.coupon = None
            orderline.coupon_real_value = 0
            orderline.cost = 0
            orderline.save()

        if order.coupon:
            retirement_orderlines = order.order_lines.filter(
                content_type__model='retirement'
            )

            retirements_id = retirement_orderlines.values_list('object_id', flat=True)

            try:
                applicable_retirement = Retirement.objects.filter(
                    id__in=retirements_id
                ).latest('price')
            except Retirement.DoesNotExist:
                continue

            applicable_orderline = retirement_orderlines.get(
                object_id=applicable_retirement.pk
            )
            applicable_orderline.coupon = order.coupon
            applicable_orderline.coupon_real_value = order.coupon.value
            applicable_orderline.cost = applicable_retirement.price - order.coupon.value
            applicable_orderline.save()


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_add_coupon_orderline'),
    ]

    operations = [
        migrations.RunPython(move_coupon_to_orderlines, migrations.RunPython.noop),
    ]