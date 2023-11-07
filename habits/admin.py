from django.contrib import admin

from habits.models import Habits


# Register your models here.

@admin.register(Habits)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('action', 'place',)
