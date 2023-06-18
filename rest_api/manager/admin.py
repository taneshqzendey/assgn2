from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import transact

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active',)
    search_fields = ('username', 'email',)
    readonly_fields = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(CustomUser, CustomUserAdmin)

"""class transactadmin(models.Manager):
    list_display = ('payer', 'payee', 'amount','transactid')
    search_fields = ('transactid')
    readonly_fields = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(CustomUser, CustomUserAdmin)
"""