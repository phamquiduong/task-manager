from django.contrib import admin

from session import models


class SessionAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_agent', 'expired_datetime')
    search_fields = ('user_id',)
    list_filter = ('user_id',)


admin.site.register(models.Session, SessionAdmin)
