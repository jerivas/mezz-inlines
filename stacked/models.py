from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from mezzanine.core.models import Orderable, RichText


@python_2_unicode_compatible
class Family(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        verbose_name = "family"
        verbose_name_plural = "families"

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class FamilyMember(Orderable, RichText):
    family = models.ForeignKey(Family, related_name="members")
    name = models.CharField(max_length=50)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Pet(Orderable):
    family = models.ForeignKey(Family, related_name="pets")
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
