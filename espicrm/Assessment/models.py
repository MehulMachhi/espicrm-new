from DetailEnquiry.models import Detail_Enquiry
# Create your models here.
from Master.models import course_levels , intake , Course , university , assessment_status
from django.contrib.auth import get_user_model
from django.db import models
from django_countries.fields import CountryField


class assessment(models.Model):
    assigned_users = models.ForeignKey(get_user_model() , on_delete=models.CASCADE)
    enquiry = models.ForeignKey(Detail_Enquiry , on_delete=models.CASCADE)
    student_country = CountryField(blank_label="(select country)" , blank=True , null=True)
    university = models.ForeignKey(university , on_delete=models.CASCADE , blank=True , null=True)
    level_applying_for = models.ForeignKey(course_levels , on_delete=models.CASCADE , blank=True , null=True)
    course_interested = models.ForeignKey(Course , on_delete=models.CASCADE , blank=True , null=True)
    intake_interested = models.ForeignKey(intake , on_delete=models.CASCADE , blank=True , null=True)
    specialisation = models.CharField(max_length=100 , blank=True , null=True)
    duration = models.CharField(max_length=100 , blank=True , null=True)
    application_fee = models.CharField(max_length=100 , blank=True , null=True)
    tution_fee = models.CharField(max_length=100 , blank=True , null=True)
    fee_currency = models.CharField(max_length=100 , blank=True , null=True)
    course_link = models.CharField(max_length=200 , blank=True , null=True)
    ass_status = models.ForeignKey(assessment_status , blank=True , on_delete=models.CASCADE , null=True)
    notes = models.TextField(blank=True , null=True)

    def __str__(self):
        return (f"{self.enquiry}")
