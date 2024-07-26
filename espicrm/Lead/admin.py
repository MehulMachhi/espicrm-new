# Register your models here.
from django.contrib import admin

from .models import Lead


class LeadAdmin(admin.ModelAdmin):
    list_display = (
    'name' , 'phone_no' , 'email_id' , 'country' , 'purpose' , 'source_of_enquiry' , 'assigned_to' , 'timestamp')
    list_filter = ('country' , 'purpose' , 'source_of_enquiry' , 'assigned_to')
    search_fields = ('name' , 'phone_no' , 'email_id' , 'remark')
    fieldsets = (
        (None , {
            'fields': (
            'name' , 'phone_no' , 'email_id' , 'country' , 'purpose' , 'source_of_enquiry' , 'assigned_to' , 'remark' ,
            'follow_up')
        }) ,
    )


admin.site.register(Lead , LeadAdmin)
