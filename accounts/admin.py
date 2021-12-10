from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

# Register your models here.


class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    search_fields = ['email', 'first_name']
    readonly_fields = ('last_login', 'date_joined',)
    ordering = ('-date_joined',)
    
    filter_horizontal = ()
    list_filter = ('username', 'email', 'first_name', 'last_name',)
    fieldsets = ()


admin.site.register(Account, AccountAdmin)