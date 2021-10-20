from django.contrib import admin
from beans.models import Bean, TastingNote

@admin.register(Bean)
class BeanAdmin(admin.ModelAdmin):
    pass


@admin.register(TastingNote)
class TastingNoteAdmin(admin.ModelAdmin):
    pass