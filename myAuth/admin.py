from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser

# Isso garante que os seus novos campos apareçam no painel de edição do Django Admin
class MyUserAdmin(UserAdmin):
    model = MyUser
    # Adiciona os novos campos nas seções do formulário do Admin
    fieldsets = UserAdmin.fieldsets + (
        ('Informações Adicionais', {'fields': ('points', 'country', 'ddd','phone', 'language')}),
    )

admin.site.register(MyUser, MyUserAdmin)
# Register your models here.
