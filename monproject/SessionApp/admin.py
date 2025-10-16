from django.contrib import admin
from .models import Session
#admin.site.register(Session)
@admin.register(Session)
class AdminSessionModel(admin.ModelAdmin):
    list_display=("title","topic","session_day","start_time","end_time")
    ordering=("session_day",)
    list_filter=("topic",)
    search_fields=("title",)
    fieldsets=(
        ("information generale",{
            "fields":("session_id","title","topic","room")
        }),
        ("logistics info",{
            "fields":("session_day","start_time","end_time")
        })
    ) 
    readonly_fields=("session_id",)
    
# Register your models here.
