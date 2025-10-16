from django.contrib import admin
from .models import Conference, Submission, Organisation
# Register your models here.
admin.site.site_title="Gestion Conférence 25-26 "
admin.site.site_header="Gestion Conférences"
admin.site.index_title="django App conférence"
#admin.site.register(Conference)
admin.site.register(Submission)
admin.site.register(Organisation)
class SubmissionInline(admin.StackedInline):
    model = Submission
    extra= 1
    readonly_fields=("submission_date",)



@admin.register(Conference)
class AdminConferenceModel(admin.ModelAdmin):
    list_display=("name","theme","start_date","end_date","duration")
    ordering=("start_date",)
    list_filter=("theme",)
    search_fields=("description","name")
    date_hierarchy="start_date"
    fieldsets=(
        ("information generale",{
            "fields":("conference_id","name","theme","description")
        }),
        ("logistics info",{
            "fields":("location","start_date","end_date")
        })
    ) 
    readonly_fields=("conference_id",)
    def duration(self,objet):
        if objet.start_date and objet.end_date:
            return (objet.end_date-objet.start_date).days
        return "rien a signaler"
    duration.short_description="Duration (days)"
    
    inlines=[SubmissionInline]
# Register your models here.
