# Create your models here.
from Enquiry.models import enquiry
from Master.models import (Edu_Level , Work_Experience , Toefl_Exam , ielts_Exam , PTE_Exam ,
                           Duolingo_Exam , Gre_Exam , Gmat_Exam , Rejection_Reason , Available_Services ,
                           Detail_Enquiry_Status)
from django.db import models


class Detail_Enquiry(models.Model):
    Current_Enquiry = models.ForeignKey(enquiry , on_delete=models.CASCADE)
    Current_Education_Details = models.ForeignKey(Edu_Level , on_delete=models.CASCADE , blank=True , null=True)
    Tenth_Education_Details = models.ForeignKey(Edu_Level , on_delete=models.CASCADE , blank=True , null=True ,
                                                related_name='Tenth_Education_Details')
    Twelveth_Education_Details = models.ForeignKey(Edu_Level , on_delete=models.CASCADE , blank=True , null=True ,
                                                   related_name='Twelveth_Education_Details')
    Graduation_Education_Details = models.ForeignKey(Edu_Level , on_delete=models.CASCADE , blank=True , null=True ,
                                                     related_name='Graduation_Education_Details')
    Work_Experience = models.ForeignKey(Work_Experience , max_length=100 , on_delete=models.CASCADE , blank=True ,
                                        null=True)
    Toefl_Exam = models.ForeignKey(Toefl_Exam , on_delete=models.CASCADE , blank=True , null=True)
    ielts_Exam = models.ForeignKey(ielts_Exam , on_delete=models.CASCADE , blank=True , null=True)
    PTE_Exam = models.ForeignKey(PTE_Exam , on_delete=models.CASCADE , blank=True , null=True)
    Duolingo_Exam = models.ForeignKey(Duolingo_Exam , on_delete=models.CASCADE , blank=True , null=True)
    Gre_Exam = models.ForeignKey(Gre_Exam , on_delete=models.CASCADE , blank=True , null=True)
    Gmat_Exam = models.ForeignKey(Gmat_Exam , on_delete=models.CASCADE , blank=True , null=True)
    Father_Occupation = models.CharField(max_length=100 , blank=True , null=True)
    Father_Annual_Income = models.FloatField(blank=True , null=True)
    Refusal = models.ForeignKey(Rejection_Reason , on_delete=models.CASCADE , blank=True , null=True)
    Twelveth_Document = models.FileField(upload_to='documents/' , blank=True)
    Tenth_Document = models.FileField(upload_to='documents/' , blank=True)
    Graduation_Marksheet = models.FileField(upload_to='documents/' , blank=True)
    Graduation_Certificate = models.FileField(upload_to='documents/' , blank=True)
    UG_Marksheet = models.FileField(upload_to='documents/' , blank=True)
    UG_Certificate = models.FileField(upload_to='documents/' , blank=True)
    Work_Experience_Document = models.FileField(upload_to='documents/' , blank=True)
    Passport_Document = models.FileField(upload_to='documents/' , blank=True)
    Offer_Letter = models.FileField(upload_to='documents/' , blank=True)
    Ielts_Result = models.FileField(upload_to='documents/' , blank=True)
    Toefl_Result = models.FileField(upload_to='documents/' , blank=True)
    PTE_Result = models.FileField(upload_to='documents/' , blank=True)
    Duolingo_Result = models.FileField(upload_to='documents/' , blank=True)
    Gre_Result = models.FileField(upload_to='documents/' , blank=True)
    Gmat_Result = models.FileField(upload_to='documents/' , blank=True)
    Confirmed_Services = models.ManyToManyField(Available_Services , blank=True)
    Enquiry_Status = models.ForeignKey(Detail_Enquiry_Status , on_delete=models.CASCADE , blank=True , null=True)

    def __str__(self):
        return (f"{self.Current_Enquiry}")
