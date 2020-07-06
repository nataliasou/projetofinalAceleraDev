from django.contrib import admin

from api.models import Log, User, ErrorInstances, Group

@admin.register(Log)
class LogModeEvent(admin.ModelAdmin):
    list_display = ('title', 'date')

@admin.register(User)
class UserModeEvent(admin.ModelAdmin):
    list_display = ('name', 'email')

@admin.register(ErrorInstances)
class ErrorInstancesModeEvent(admin.ModelAdmin):
    list_display = ('level', 'events', 'type_error', 'shelved', 'user_id', 'error')
    list_filter = ('level', 'events')

admin.site.register(Group)