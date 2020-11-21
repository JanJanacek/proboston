from django.contrib import admin
from web.models import Users


class UsersAdmin(admin.ModelAdmin):
    search_fields = ['email', 'ico']

admin.site.register(Users, UsersAdmin)