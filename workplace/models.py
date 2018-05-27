from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.html import format_html
from django.contrib.auth import get_user_model

from location.models import Address

User = get_user_model()


class Workplace(models.Model):
    """Represents physical places."""

    class Meta:
        verbose_name = _("Workplace")
        verbose_name_plural = _("Workplaces")

    name = models.CharField(
        verbose_name=_("Name"),
        max_length=253,
    )

    details = models.CharField(
        verbose_name=_("Details"),
        max_length=1000,
    )

    seats = models.IntegerField(
        verbose_name=_("Seats"),
    )

    location = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,
        related_name="location",
    )

    def __str__(self):
        return self.name


class Picture(models.Model):
    """Represents pictures representing a workplace"""

    class Meta:
        verbose_name = _("Picture")
        verbose_name_plural = _("Pictures")

    name = models.CharField(
        verbose_name=_("Name"),
        max_length=253,
    )

    workplace = models.ForeignKey(
        Workplace,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name=_("Workplace"),
        related_name='pictures',
    )

    picture = models.ImageField(
        _('picture'),
        upload_to='workplaces'
    )

    # Needed to display in the admin panel
    def picture_tag(self):
        return format_html(
            '<img href="{0}" src="{0}" height="150" />'
            .format(self.picture.url)
        )

    picture_tag.allow_tags = True
    picture_tag.short_description = 'Picture'

    def __str__(self):
        return self.name


class Period(models.Model):
    """Represents periods of time that has certain attributes"""

    class Meta:
        verbose_name = _("Period")
        verbose_name_plural = _("Periods")

    name = models.CharField(
        verbose_name=_("Name"),
        max_length=253,
    )

    workplace = models.ForeignKey(
        Workplace,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name=_("Workplace"),
        related_name='periods',
    )

    price = models.PositiveIntegerField(
        verbose_name=_("Price"),
    )

    start_date = models.DateTimeField(
        verbose_name=_("Start Date"),
        blank=True,
    )

    end_date = models.DateTimeField(
        verbose_name=_("End Date"),
        blank=True,
    )

    is_active = models.BooleanField(
        verbose_name=_("Activation"),
        default=False,
    )

    def __str__(self):
        return self.name


class TimeSlot(models.Model):
    """Represents time slots in a day"""

    class Meta:
        verbose_name = _("Time slot")
        verbose_name_plural = _("Time slots")

    name = models.CharField(
        verbose_name=_("Name"),
        max_length=253,
    )

    period = models.ForeignKey(
        Period,
        on_delete=models.CASCADE,
        verbose_name=_("Period"),
        related_name='time_slots',
    )

    users = models.ManyToManyField(
        User,
        blank=True,
        verbose_name=_("User"),
        related_name='time_slots',
    )

    price = models.PositiveIntegerField(
        verbose_name=_("Price"),
        blank=True,
        null=True,
    )

    start_time = models.TimeField(
        verbose_name=_("Start time"),
    )

    end_time = models.TimeField(
        verbose_name=_("End time"),
    )

    day = models.DateField(
        verbose_name=_("Day"),
    )

    def __str__(self):
        return self.name
