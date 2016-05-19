from __future__ import unicode_literals

from django.contrib import admin

from mezzanine.core.admin import StackedDynamicInlineAdmin, TabularDynamicInlineAdmin

from .models import Family, Pet, FamilyMember


class FamilyMemberInlineAdmin(StackedDynamicInlineAdmin):
    model = FamilyMember
    fields = ["name", "date_of_birth", "content"]


class PetInlineAdmin(TabularDynamicInlineAdmin):
    model = Pet


@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    inlines = [FamilyMemberInlineAdmin, PetInlineAdmin]
