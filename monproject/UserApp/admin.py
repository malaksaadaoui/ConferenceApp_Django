from django.contrib import admin
from .models import User
# Register your models here.

#admin.site.register(User)
@admin.register(User)
class AdminUserModel(admin.ModelAdmin):
    list_display=("user_id","first_name","last_name","role","email")
    ordering=("user_id",)
    list_filter=("nationality",)
    search_fields=("email",)
    fieldsets=(
        ("Informations personnelles",{
            "fields":("first_name","last_name","nationality","email")
        }),
    ) 
    readonly_fields=("user_id",)
    
# Register your models here.
