from django.contrib import admin
from . import models

@admin.register(models.Notification)
class NotificationcAdmin(admin.ModelAdmin):
    
    list_display = (
        'creator',
        'to',
        'notification_type',
    )