from django.contrib import admin
from .models import Product,Task

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name","price","public")
    list_filter = ("name","price","public")
    search_fields = ("name","price","public")
    readonly_fields = ("public",)

class TaskAdmin(admin.ModelAdmin):
    list_display = ("name","points","duration")
    list_filter = ("name","points","duration")
    search_fields = ("name","points","duration")

admin.site.register(Product,ProductAdmin)
admin.site.register(Task,TaskAdmin)