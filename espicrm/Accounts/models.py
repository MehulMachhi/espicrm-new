from DetailEnquiry.models import Detail_Enquiry
from Master.models import Payment_Type , Payment_Status , Payment_Mode , Available_Services
from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class Payment(models.Model):
    Memo_For = models.ForeignKey(Detail_Enquiry , on_delete=models.CASCADE , blank=True , )
    payment_id = models.CharField(max_length=100 , blank=True , null=True)
    Payment_Type = models.ForeignKey(Payment_Type , on_delete=models.CASCADE , blank=True)
    Payment_For = models.ManyToManyField(Available_Services , blank=True)
    payment_date = models.DateField(blank=True , null=True , editable=True)
    payment_amount = models.FloatField(blank=True , null=True)
    payment_mode = models.ForeignKey(Payment_Mode , on_delete=models.CASCADE , blank=True)
    payment_status = models.ForeignKey(Payment_Status , on_delete=models.CASCADE , blank=True)
    payment_reference = models.CharField(max_length=100 , blank=True , null=True)
    payment_remarks = models.TextField(blank=True , null=True)
    payment_received_by = models.ForeignKey(get_user_model() , on_delete=models.CASCADE , default="" , blank=True ,
                                            null=True)
    payment_document = models.FileField(upload_to='documents/' , blank=True)

    # payment_user = models.ForeignKey('Accounts.CustomUser', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return (f"{self.payment_id}")
