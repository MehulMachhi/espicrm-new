from Assessment.models import assessment
from Master.models import application_status
from django.db import models


# Create your models here.
class Application(models.Model):
    application = models.ForeignKey(assessment , on_delete=models.CASCADE)
    sop = models.FileField(upload_to='sop' , blank=True , null=True)
    cv = models.FileField(upload_to='cv' , blank=True , null=True)
    passport = models.FileField(upload_to='passport' , blank=True , null=True)
    ielts = models.FileField(upload_to='ielts' , blank=True , null=True)
    gre = models.FileField(upload_to='gre' , blank=True , null=True)
    toefl = models.FileField(upload_to='toefl' , blank=True , null=True)
    gmat = models.FileField(upload_to='gmat' , blank=True , null=True)
    pte = models.FileField(upload_to='pte' , blank=True , null=True)
    work_experience = models.FileField(upload_to='work_experience' , blank=True , null=True)
    diploma_marksheet = models.FileField(upload_to='diploma_marksheet' , blank=True , null=True)
    bachelor_marksheet = models.FileField(upload_to='bachelor_marksheet' , blank=True , null=True)
    master_marksheet = models.FileField(upload_to='master_marksheet' , blank=True , null=True)
    other_documents = models.FileField(upload_to='other_documents' , blank=True , null=True)
    application_status = models.ForeignKey(application_status , max_length=100 , blank=True , on_delete=models.CASCADE ,
                                           null=True)

    def __str__(self):
        return (f"{self.application}")
