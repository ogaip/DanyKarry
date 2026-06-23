from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import Usuario

# Register your models here.


class UsuarioAdminForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        widgets = {
            'pin_autorizacion': forms.PasswordInput(render_value=True)
        }


class UsuarioAdmin(UserAdmin):
    form = UsuarioAdminForm
    list_display = ('username', 'email', 'rol', 'is_staff', 'is_active')

    list_filter = ('rol', 'is_staff', 'is_active')

    fieldsets = UserAdmin.fieldsets + (
        ('Informacion de Roles (POS)', {
         'fields': ('rol', 'pin_autorizacion')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Informacion de Roles (POS)', {
         'fields': ('rol', 'pin_autorizacion')}),
    )


admin.site.register(Usuario, UsuarioAdmin)
