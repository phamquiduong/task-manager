from django.contrib import admin
from django.utils.html import format_html

from authentication import forms, models
from authentication.helpers.static_helper import StaticHelper


class UserAdmin(admin.ModelAdmin):
    form = forms.UserForm
    list_display = ('username', 'email', 'full_name', 'get_avatar_url')
    search_fields = ('username', 'email', 'full_name')
    list_filter = ('username', 'email')

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.static_helper = StaticHelper()

    def get_avatar_url(self, obj):
        url = self.static_helper.get_avtar_url(key=obj.avatar_key)
        if obj.avatar_key:
            return format_html('<a href="{}" target="_blank">{}</a>', url, obj.avatar_key)
        return '-'

    get_avatar_url.short_description = 'Avatar URL'


admin.site.register(models.User, UserAdmin)
