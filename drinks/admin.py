from django.contrib import admin

from drinks.models import Beer


@admin.register(Beer)
class BeerAdmin(admin.ModelAdmin):
    pass
