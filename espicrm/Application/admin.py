from django.contrib import admin

from .models import Application


class ApplicationAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('application' , 'application_status' , 'sop' , 'cv' , 'passport')

    # Enable search functionality
    search_fields = ('application__enquiry__Current_Enquiry__student_First_Name' ,
                     'application_status__status')  # Assuming 'status' field in 'application_status'

    # Organize form fields into fieldsets for the detailed view
    fieldsets = (
        ('Application Details' , {
            'fields': ('application' , 'application_status')
        }) ,
        ('Academic Documents' , {
            'fields': ('diploma_marksheet' , 'bachelor_marksheet' , 'master_marksheet')
        }) ,
        ('Test Scores & Other Documents' , {
            'fields': ('ielts' , 'gre' , 'toefl' , 'gmat' , 'pte' , 'work_experience' , 'other_documents')
        }) ,
        ('Personal Documents' , {
            'fields': ('sop' , 'cv' , 'passport')
        }) ,
    )


admin.site.register(Application , ApplicationAdmin)
