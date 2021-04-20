from django.contrib import admin
from .models import LoginUser
from .forms import LoginUserChangeForm, LoginUserCreationForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class LoginUserAdmin(UserAdmin):
    add_form = LoginUserChangeForm
    form = LoginUserCreationForm
    model = LoginUser
    list_display = ('email', 'is_staff', 'is_active', 'name')
    list_filter = ('email', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
                'classes': ('wide',),
                'fields': ('email', 'name', 'password1', 'is_staff', 'is_active')}),
    )
    search_fields = ('email', 'name')
    ordering = ('email', )


# admin.site.register(WWFUser, WWFUserAdmin)
admin.site.register(LoginUser,LoginUserAdmin)
