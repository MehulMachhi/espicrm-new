# Register your models here.
from django.contrib import admin

from .models import assessment


class AssessmentAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = (
    'enquiry' , 'student_country' , 'university' , 'level_applying_for' , 'course_interested' , 'intake_interested' ,
    'specialisation' , 'application_fee' , 'tution_fee')

    # Fields to enable search functionality
    search_fields = (
    'enquiry__Current_Enquiry__student_First_Name' , 'university__univ_name' , 'course_interested__name' ,
    'level_applying_for__name')

    # Organize form fields into fieldsets for detailed view
    fieldsets = (
        ('Assessment Information' , {
            'fields': ('assigned_users' , 'enquiry' , 'student_country')
        }) ,
        ('University and Course Details' , {
            'fields': (
            'university' , 'level_applying_for' , 'course_interested' , 'intake_interested' , 'specialisation' ,
            'duration' , 'application_fee' , 'tution_fee' , 'fee_currency' , 'course_link')
        }) ,
        ('Additional Information' , {
            'fields': ('notes' ,)
        }) ,
    )

    # Optionally, you can specify filters for the list view to allow filtering by certain criteria
    list_filter = ('student_country' , 'university' , 'level_applying_for' , 'intake_interested')


admin.site.register(assessment , AssessmentAdmin)
