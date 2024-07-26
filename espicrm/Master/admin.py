from Master.models import twelfth_std_percentage_requirement , bachelor_requirement , masters_requirement , \
    tenth_std_percentage_requirement , \
    ielts_Exam , PTE_Exam , Toefl_Exam , Duolingo_Exam , Gre_Exam , Gmat_Exam , Available_Services , \
    Detail_Enquiry_Status , Enquiry_Source , Payment_Type , \
    Payment_Status , Payment_Mode
from django.contrib import admin
from import_export.admin import ImportExportMixin

# Register your models here.
from .models import country , course_levels , intake , current_education , documents_required , \
    enquiry_status , application_status , Course , university , assessment_status , Edu_Level , Work_Experience , \
    Rejection_Reason , AdmissionStatus , SubStatus , VisaStatus , VisaSubStatus, campus
from .resources import CourseResource , UniversityResource


# Register your models here.


class CourseListAdmin(ImportExportMixin , admin.ModelAdmin):
    resource_class = CourseResource

    list_display = (
        'id' , 'university' , 'course_name' , 'course_levels' , 'display_intakes' ,
        'tenth_std_percentage_requirement' , 'twelfth_std_percentage_requirement' ,
        'bachelor_requirement' , 'masters_requirement' , 'Toefl_Exam' , 'ielts_Exam' ,
        'PTE_Exam' , 'Duolingo_Exam' , 'Gre_Exam' , 'Gmat_Exam' , 'Remark' , 'Active'
    )

    list_filter = (
        'university' , 'course_name' , 'course_levels' , 'intake' , 'documents_required' ,
        'tenth_std_percentage_requirement' , 'twelfth_std_percentage_requirement' ,
        'bachelor_requirement' , 'masters_requirement' , 'Toefl_Exam' , 'ielts_Exam' ,
        'PTE_Exam' , 'Duolingo_Exam' , 'Gre_Exam' , 'Gmat_Exam' , 'Active'
    )

    fieldsets = (
        ('Course Details' , {
            'fields': ('university' ,  'Univ_Campus' ,'course_name' , 'course_levels' , 'intake' , 'documents_required' , 'Active')
        }) ,
        ('Course Requirements' , {
            'fields': (
                'tenth_std_percentage_requirement' , 'twelfth_std_percentage_requirement' ,
                'bachelor_requirement' , 'masters_requirement' , 'Toefl_Exam' , 'ielts_Exam' ,
                'PTE_Exam' , 'Duolingo_Exam' , 'Gre_Exam' , 'Gmat_Exam'
            )
        }) ,
        ('Notes' , {
            'fields': ('Remark' ,)
        }) ,
    )

    list_display_links = ('id' , 'university' ,)
    list_per_page = 20
    search_fields = ('course_name' , 'university__name' , 'country__country_name')

    def display_intakes(self , obj):
        """
        Returns a comma-separated list of intake months and years from the ManyToManyField.
        """
        return ", ".join(
            [f"{intake.intake_Name} {intake.intake_month} {intake.intake_year}" for intake in obj.intake.all()])

    display_intakes.short_description = 'Intakes'  # Sets the column name in the admin list view


class UniversityAdmin(ImportExportMixin , admin.ModelAdmin):
    resource_class = UniversityResource

    list_display = (
        'id' , 'univ_name' , 'country' , 'deadline' , 'moi_accepted' , 'Application_fee' , 'Active'
    )

    list_filter = (
        'country' , 'levels' , 'moi_accepted' , 'Active'
    )

    search_fields = (
        'univ_name' , 'country__country_name' , 'levels__levels' , 'univ_email'
    )

    fieldsets = (
        ('Basic Information' , {
            'fields': ('univ_name' , 'country' , 'levels' , 'univ_desc' , 'univ_logo' , 'newsletter')
        }) ,
        ('Application Details' , {
            'fields': ('deadline' , 'moi_accepted' , 'Application_form' , 'Application_form_link' , 'Application_fee' ,
                       'Admission_Requirements' , 'Backlogs_allowed')
        }) ,
        ('Contact Information' , {
            'fields': ('univ_phone' , 'univ_email' , 'univ_website')
        }) ,
        ('Requirements' , {
            'fields': (
                'tenth_std_percentage_requirement' , 'twelfth_std_percentage_requirement' ,
                'bachelor_requirement' , 'masters_requirement' , 'Toefl_Exam' , 'ielts_Exam' ,
                'PTE_Exam' , 'Duolingo_Exam' , 'Gre_Exam' , 'Gmat_Exam'
            )
        }) ,
        ('Additional Information' , {
            'fields': ('Remark' , 'Active' , 'assigned_users')
        }) ,
    )

    list_display_links = ('id' , 'univ_name')
    list_per_page = 20

    

class SubStatusInline(admin.TabularInline):
    model = SubStatus
    extra = 1


class AdmissionStatusAdmin(admin.ModelAdmin):
    inlines = [SubStatusInline]
    list_display = ('status_name' ,)


class VisaSubStatusInline(admin.TabularInline):
    model = VisaSubStatus
    extra = 1


class VisaStatusAdmin(admin.ModelAdmin):
    inlines = [VisaSubStatusInline]
    list_display = ('status_name' ,)


class CountryAdmin(admin.ModelAdmin):
    fieldsets = (
        (None , {
            'fields': ('country_name' , 'currency')
        }) ,
        ('Admission Process' , {
            'fields': ('admission_process_notes' , 'admission_process_attachment')
        }) ,
        ('Visa Process' , {
            'fields': ('visa_process_notes' , 'visa_process_attachment')
        }) ,
        ('Attachments' , {
            'fields': ('news_letter' , 'video_attachment' , 'country_brochure')
        }) ,
        ('Statuses' , {
            'fields': ('admission_status' , 'visa_status')
        }) ,
    )

    list_display = ('country_name' , 'currency')
    search_fields = ('country_name' , 'currency')
    list_filter = ('admission_status' , 'visa_status')
    filter_horizontal = ('admission_status' , 'visa_status')


admin.site.register(course_levels)
admin.site.register(intake)
admin.site.register(current_education)
admin.site.register(documents_required)
admin.site.register(enquiry_status)
admin.site.register(application_status)
admin.site.register(Course , CourseListAdmin)
admin.site.register(university , UniversityAdmin)
admin.site.register(assessment_status)
admin.site.register(Edu_Level)
admin.site.register(Work_Experience)
admin.site.register(ielts_Exam)
admin.site.register(PTE_Exam)
admin.site.register(Toefl_Exam)
admin.site.register(Duolingo_Exam)
admin.site.register(Gre_Exam)
admin.site.register(Gmat_Exam)
admin.site.register(Rejection_Reason)
admin.site.register(tenth_std_percentage_requirement)
admin.site.register(twelfth_std_percentage_requirement)
admin.site.register(bachelor_requirement)
admin.site.register(masters_requirement)
admin.site.register(Available_Services)
admin.site.register(Detail_Enquiry_Status)
admin.site.register(Enquiry_Source)
admin.site.register(Payment_Type)
admin.site.register(Payment_Status)
admin.site.register(Payment_Mode)
admin.site.register(AdmissionStatus , AdmissionStatusAdmin)
admin.site.register(SubStatus)
admin.site.register(VisaStatus , VisaStatusAdmin)
admin.site.register(VisaSubStatus)
admin.site.register(country , CountryAdmin)
admin.site.register(campus)

# Register your models here.
