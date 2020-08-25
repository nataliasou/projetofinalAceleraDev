from django.contrib import admin

from api.models import ErrorInstances

@admin.register(ErrorInstances)
class ErrorInstancesModeEvent(admin.ModelAdmin):
    list_display = (
        'title',
        'date',
        'level',
        'events',
        'type_error',
        'shelved',
        'user_id'
    )
    list_filter = ('level', 'events')