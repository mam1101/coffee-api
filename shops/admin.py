from django.contrib import admin

from shops.models import Address, Cafe, Distributer, OperatingHours, Roastery


@admin.register(Cafe)
class CafeAdmin(admin.ModelAdmin):
    pass


@admin.register(Distributer)
class DistributerAdmin(admin.ModelAdmin):
    pass


@admin.register(Roastery)
class RoasteryAdmin(admin.ModelAdmin):
    pass


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass

@admin.register(OperatingHours)
class OperatingHoursAdmin(admin.ModelAdmin):
    pass
