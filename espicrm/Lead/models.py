from Followup.models import Followups
from Master.models import country , Available_Services
from django.contrib.auth import get_user_model
from django.db import models


class Lead(models.Model):
    name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=15)
    email_id = models.EmailField()
    country = models.ForeignKey(country , on_delete=models.CASCADE)
    purpose = models.ForeignKey(Available_Services , on_delete=models.CASCADE , verbose_name="Purpose")
    source_of_enquiry = models.ForeignKey('Master.Enquiry_Source' , on_delete=models.CASCADE ,
                                          verbose_name="Source of Enquiry")
    assigned_to = models.ForeignKey(get_user_model() , on_delete=models.CASCADE , verbose_name="For Counsellor")
    remark = models.TextField(blank=True , null=True)
    follow_up = models.ForeignKey(Followups , on_delete=models.CASCADE , blank=True , null=True ,
                                  verbose_name="Follow-up")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Create your models here.
