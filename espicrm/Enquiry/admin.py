from Master.models import enquiry_status
from django.contrib import admin
from import_export.admin import ImportExportMixin
from .adminnew.custom_admin import custom_admin_site
from .models import enquiry


class EnquiryList(ImportExportMixin , admin.ModelAdmin):
    fieldsets = (
        ("Student Info" ,
         {"fields": ("student_First_Name" , "student_Last_Name" , "student_passport" , 'Source_Enquiry')}) ,
        ("Contact Info" , {"fields": (
            "student_phone" , "alternate_phone" , "student_email" , "student_address" , "student_country" ,
            "student_state" ,
            "student_city" , "student_zip")}) ,
        ("Education Info" , {"fields": ("current_education" ,)}) ,
        ("Enquiry Info" , {"fields": (
            "country_interested" , "university_interested" , "level_applying_for" , "course_interested" ,
            "intake_interested" , "Interested_Services")}) ,
        ("For Counsellor" , {"fields": ("assigned_users" , "enquiry_status" , "notes" , 'followup_create' ,)}) ,
    )

    jazzmin_section_order = ("Student Info" , "Contact Info" , "Education Info" , "Enquiry Info" , "For Counsellor")

    actions = ['update_enquiry_status']
    list_display = (
        'student_First_Name' , 'student_Last_Name' , 'student_phone' , 'student_email' , 'display_country_interested' ,
        'display_university_interested' , 'Interested_service' ,
        'display_course_interested'  , 'intake_interested' ,
        'assigned_users' , 'enquiry_status' , 'notes' ,  'Source_Enquiry'
    )

    list_filter = (
        'student_First_Name' , 'student_phone' , 'student_email' , 'current_education' ,
        'university_interested' , 'course_interested' , 'assigned_users' , 'enquiry_status' , 'Source_Enquiry'
    )

    list_display_links = ('student_First_Name' ,)
    list_per_page = 10

    search_fields = (
    'student_First_Name' , 'student_Last_Name' , 'student_phone' , 'student_email' , 'current_education' ,
    'country_interested__country_name' , 'university_interested__univ_name' ,
    'course_interested__course_name' , 'level_applying_for__level_name' , 'intake_interested__intake_Name' ,
    'assigned_users__username' , 'enquiry_status__status')

    def update_enquiry_status(modeladmin , request , queryset):
        processed_status = enquiry_status.objects.get(status='Processed')
        queryset.update(enquiry_status=processed_status)

    update_enquiry_status.short_description = "Update status to Processed"

    def Interested_service(self , obj):
        return ', '.join([a.Services for a in obj.Interested_Services.all()])

    Interested_service.short_description = 'Interested Services'

   

    def display_country_interested(self , obj):
        return ', '.join([country.country_name for country in obj.country_interested.all()])

    display_country_interested.short_description = 'Country Interested'

    def display_university_interested(self , obj):
        return obj.university_interested.univ_name

    display_university_interested.short_description = 'University Interested'

    def display_course_interested(self , obj):
        return obj.course_interested.course_name

    display_course_interested.short_description = 'Course Interested'

    # def display_level_applying_for(self , obj):
    #     return obj.level_applying_for.level_name

    # display_level_applying_for.short_description = 'Level Applying For'


admin.site.register(enquiry , EnquiryList)


