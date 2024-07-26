# Register your models here.
from django.contrib import admin

from .models import Followups , FollowupStatus , Task


class TaskInline(admin.TabularInline):
    model = Followups.tasks.through
    extra = 1


class FollowupAdmin(admin.ModelAdmin):
    inlines = [TaskInline]
    list_display = ('followup_date' , 'followup_status' , 'assigned_to' , 'next_followup_date')
    list_filter = ('followup_date' , 'followup_status' , 'assigned_to')
    search_fields = ('enquiry__student_First_Name' , 'enquiry__student_Last_Name' , 'notes')
    fieldsets = (
        (None , {
            'fields': ('followup_status' , 'notes' , 'assigned_to' , 'next_followup_date')
        }) ,
    )

    def display_tasks(self , obj):
        return ", ".join([task.task_name for task in obj.tasks.all()])

    display_tasks.short_description = 'Tasks'


class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_name' , 'assigned_to' , 'due_date' , 'completed')
    list_filter = ('due_date' , 'assigned_to' , 'completed')
    search_fields = ('task_name' , 'task_description')
    fieldsets = (
        (None , {
            'fields': ('task_name' , 'task_description' , 'assigned_to' , 'due_date' , 'completed')
        }) ,
    )


class FollowupStatusAdmin(admin.ModelAdmin):
    list_display = ('status_name' ,)
    search_fields = ('status_name' ,)


admin.site.register(Followups , FollowupAdmin)
admin.site.register(FollowupStatus , FollowupStatusAdmin)
admin.site.register(Task , TaskAdmin)
