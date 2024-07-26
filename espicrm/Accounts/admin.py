from django.contrib import admin
from django.db.models import Sum

from .models import Payment


# Register your models here.


class PaymentListAdmin(admin.ModelAdmin):
    list_display = (
    'payment_id' , 'Payment_Type' , 'Payment' , 'payment_date' , 'payment_amount' , 'payment_mode' , 'payment_status' ,
    'payment_reference' , 'payment_remarks' , 'payment_document' , 'Pending_Amount')

    list_filter = ('payment_id' , 'Payment_Type' , 'Payment_For' , 'payment_date' , 'payment_amount' , 'payment_mode' ,
                   'payment_status' , 'payment_reference' , 'payment_remarks' , 'payment_document')

    fieldsets = (('Payment Details' , {
        'fields': ('Memo_For' , 'payment_id' , 'Payment_Type' , 'Payment_For' , 'payment_date' , 'payment_amount' ,
                   'payment_mode' , 'payment_status' , 'payment_reference' , 'payment_remarks' , 'payment_document' ,
                   'payment_received_by' ,)
    }) ,
                 )

    def Payment(self , obj):
        return ', '.join([a.Services for a in obj.Payment_For.all()])

    def Pending_Amount(self , obj):
        confirmed_amount = obj.Payment_For.aggregate(total=Sum('Price'))['total'] or 0
        # Assuming `total_amount` is a field on your `Payment` model representing the total payable amount
        pending_amount = confirmed_amount - obj.payment_amount
        return pending_amount

    Pending_Amount.short_description = "Pending Amount"


admin.site.register(Payment , PaymentListAdmin)
