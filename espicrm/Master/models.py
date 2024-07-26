from django.contrib.auth import get_user_model
from django.db import models
from django_countries.fields import CountryField
from tagging.fields import TagField
# from django.utils import six
# import six


# from Master.models import Toefl_Exam, ielts_Exam, PTE_Exam, Duolingo_Exam, Gre_Exam, Gmat_Exam, bachelor_requirement


# Create your models here.

# this is for admission stages and sub stages

class AdmissionStatus(models.Model):
    status_name = models.CharField(max_length=100 , unique=True , verbose_name="Status Name")

    def __str__(self):
        return self.status_name





class SubStatus(models.Model):
    STATUS_CHOICES = [
        ('Started' , 'Started') ,
        ('Pending' , 'Pending') ,
        ('Waiting' , 'Waiting') ,
    ]

    admission_status = models.ForeignKey(AdmissionStatus , related_name='substatuses' , on_delete=models.CASCADE)
    sub_status_name = models.CharField(max_length=100 , verbose_name="Sub Status Name")
    Admission_sub_sub = models.CharField(max_length=20 , choices=STATUS_CHOICES , verbose_name="Your Sub Status")
    remarks = models.TextField(verbose_name="Remarks" , blank=True , null=True)

    def __str__(self):
        return f"{self.sub_status_name} - {self.get_Admission_sub_sub_display()}"

    class Meta:
        verbose_name = "Sub Status"
        verbose_name_plural = "Sub Statuses"


# this is for Visa stages and sub stages
class VisaStatus(models.Model):
    status_name = models.CharField(max_length=100 , unique=True , verbose_name="Status Name")

    def __str__(self):
        return self.status_name


class VisaSubStatus(models.Model):
    STATUS_CHOICES = [
        ('Started' , 'Started') ,
        ('Pending' , 'Pending') ,
        ('Waiting' , 'Waiting') ,
    ]

    visa_status = models.ForeignKey(VisaStatus , related_name='substatuses' , on_delete=models.CASCADE)
    visa_sub_status_name = models.CharField(max_length=100 , verbose_name="Sub Status Name")
    visa_sub_sub = models.CharField(max_length=20 , choices=STATUS_CHOICES , verbose_name="Your Visa Sub Status")
    remarks = models.TextField(verbose_name="Remarks" , blank=True , null=True)

    def __str__(self):
        return f"{self.visa_sub_status_name} - {self.get_visa_sub_sub_display()}"

    class Meta:
        verbose_name = "Sub Status"
        verbose_name_plural = "Sub Statuses"


class country(models.Model):
    country_name = models.CharField(max_length=100 , unique=True , verbose_name="Country Name")
    currency = models.CharField(max_length=50 , verbose_name="Currency")
    admission_process_notes = models.TextField(verbose_name="Admission Process Notes" , blank=True , null=True)
    admission_process_attachment = models.FileField(upload_to='admission_process/' ,
                                                    verbose_name="Admission Process Attachment" , blank=True ,
                                                    null=True)
    visa_process_notes = models.TextField(verbose_name="Visa Process Notes" , blank=True , null=True)
    visa_process_attachment = models.FileField(upload_to='visa_process/' , verbose_name="Visa Process Attachment" ,
                                               blank=True , null=True)
    news_letter = models.FileField(upload_to='news_letters/' , verbose_name="News Letter" , blank=True , null=True)
    video_attachment = models.FileField(upload_to='videos/' , verbose_name="Video Attachment" , blank=True , null=True)
    country_brochure = models.FileField(upload_to='brochures/' , verbose_name="Country Brochure" , blank=True ,
                                        null=True)
    admission_status = models.ManyToManyField(AdmissionStatus , related_name='countries' ,
                                              verbose_name="Admission Status")
    visa_status = models.ManyToManyField(VisaStatus , related_name='countries' , verbose_name="Visa Status")

    def __str__(self):
        return self.country_name

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"


class course_levels(models.Model):
    levels = models.CharField(max_length=100)

    def __str__(self):
        return self.levels


class Available_Services(models.Model):
    Services = models.CharField(max_length=100)
    Price = models.FloatField(blank=True , null=True , help_text="Price in INR")

    def __str__(self):
        return (f"{self.Services}")


class current_education(models.Model):
    current_education = models.CharField(max_length=100)

    def __str__(self):
        return self.current_education


class intake(models.Model):
    intake_Name = models.CharField(max_length=100)
    intake_month = models.CharField(max_length=10)
    intake_year = models.CharField(max_length=10)

    def __str__(self):
        return self.intake_Name





class documents_required(models.Model):
    docu_name = models.CharField(max_length=100)

    def __str__(self):
        return self.docu_name


class course_requirements(models.Model):
    requirement = models.CharField(max_length=100)

    def __str__(self):
        return self.requirement


class enquiry_status(models.Model):
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.status


class assessment_status(models.Model):
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.status


class application_status(models.Model):
    App_status = models.CharField(max_length=20)

    def __str__(self):
        return self.App_status


class Edu_Level(models.Model):
    level = models.CharField(max_length=100 , blank=True , null=True)
    Stream = models.CharField(max_length=100 , blank=True , null=True)
    Percentage = models.FloatField(blank=True)
    Year_of_Passing = models.IntegerField(blank=True)
    Name_of_Institute = models.CharField(max_length=100 , blank=True)
    Medium_of_Education = models.CharField(max_length=100 , blank=True)
    Board = models.CharField(max_length=100 , blank=True)

    def __str__(self):
        return self.level


class Work_Experience(models.Model):
    Company_Name = models.CharField(max_length=100)
    Designation = models.CharField(max_length=100)
    Start_Date = models.DateField()
    End_Date = models.DateField()

    def __str__(self):
        return self.Company_Name


class ielts_Exam(models.Model):
    Listening = models.FloatField(null=True)
    Reading = models.FloatField(null=True)
    Writing = models.FloatField(null=True)
    Speaking = models.FloatField(null=True)
    Overall = models.FloatField(null=True)

    def __str__(self):
        return f"Overall: {self.Overall}"


class Toefl_Exam(models.Model):
    Listening = models.FloatField()
    Reading = models.FloatField()
    Writing = models.FloatField()
    Speaking = models.FloatField()
    Overall = models.FloatField()

    def __str__(self):
        return f"Overall: {self.Overall}"


class PTE_Exam(models.Model):
    Listening = models.FloatField()
    Reading = models.FloatField()
    Writing = models.FloatField()
    Speaking = models.FloatField()
    Overall = models.FloatField()

    def __str__(self):
        return f"Overall: {self.Overall}"


class Duolingo_Exam(models.Model):
    Overall = models.FloatField()

    def __str__(self):
        return f"Overall: {self.Overall}"


class Gre_Exam(models.Model):
    Verbal = models.FloatField()
    Quantitative = models.FloatField()
    Analytical = models.FloatField()
    overall = models.FloatField()

    @property
    def __str__(self):
        return f"Overall: {self.Overall}"


class Gmat_Exam(models.Model):
    Verbal = models.FloatField()
    Quantitative = models.FloatField()
    Analytical = models.FloatField()
    overall = models.FloatField()

    def __str__(self):
        return f"Overall: {self.Overall}"


class tenth_std_percentage_requirement(models.Model):
    percentage = models.FloatField()

    def __str__(self):
        return f"Required: {self.percentage}"


class twelfth_std_percentage_requirement(models.Model):
    percentage = models.FloatField()

    def __str__(self):
        return f"Required: {self.percentage}"


class bachelor_requirement(models.Model):
    requirement = models.CharField(max_length=100)

    def __str__(self):
        return f"Required: {self.requirement}"


class masters_requirement(models.Model):
    requirement = models.CharField(max_length=100)

    def __str__(self):
        return f"Required: {self.requirement}"


class Rejection_Reason(models.Model):
    Refusal_Reason = models.TextField()
    Refusal_Country = CountryField()
    Refusal_Visa_Category = models.CharField(max_length=100)
    Refusal_Date = models.DateField()
    Refusal_Letter = models.FileField(upload_to='refusal_letter/' , blank=True)

    def __str__(self):
        return self.Reason


class Detail_Enquiry_Status(models.Model):
    Status = models.CharField(max_length=100)

    def __str__(self):
        return self.Status


class Enquiry_Source(models.Model):
    Source = models.CharField(max_length=100)
    Reference_Number = models.CharField(max_length=100)

    def __str__(self):
        return self.Source


class Payment_Type(models.Model):
    Type = models.CharField(max_length=100)

    def __str__(self):
        return self.Type


class Payment_Status(models.Model):
    Status = models.CharField(max_length=100)

    def __str__(self):
        return self.Status


class Payment_Mode(models.Model):
    Mode = models.CharField(max_length=100)

    def __str__(self):
        return self.Mode


class university(models.Model):
    univ_name = models.CharField(max_length=100)
    country = models.ForeignKey(country , on_delete=models.CASCADE , blank=True , null=True)
    levels = models.ManyToManyField(course_levels , blank=True , null=True)
    univ_desc = models.CharField(max_length=1000 , blank=True , null=True)
    deadline = models.DateField(blank=True , null=True)
    moi_accepted = models.BooleanField()
    Application_form = models.FileField(upload_to='application_forms/' , blank=True , null=True)
    Application_form_link = models.URLField(blank=True , null=True)
    Application_fee = models.FloatField(blank=True , null=True)
    Admission_Requirements = models.TextField(blank=True , null=True)
    Backlogs_allowed = models.IntegerField(blank=True , null=True)
    univ_logo = models.ImageField(upload_to="media" , blank=True , null=True)
    univ_phone = models.CharField(max_length=10 , blank=True , null=True)
    univ_email = models.EmailField(max_length=254 , blank=True , null=True)
    univ_website = models.URLField(blank=True , null=True)
    tenth_std_percentage_requirement = models.ForeignKey("Master.tenth_std_percentage_requirement" ,
                                                         on_delete=models.CASCADE , blank=True , null=True)
    twelfth_std_percentage_requirement = models.ForeignKey("Master.twelfth_std_percentage_requirement" ,
                                                           on_delete=models.CASCADE , blank=True , null=True)
    bachelor_requirement = models.ForeignKey("Master.bachelor_requirement" , on_delete=models.CASCADE , blank=True ,
                                             null=True)
    masters_requirement = models.ForeignKey("Master.masters_requirement" , on_delete=models.CASCADE , blank=True ,
                                            null=True)
    Toefl_Exam = models.ForeignKey("Master.Toefl_Exam" , on_delete=models.CASCADE , blank=True , null=True)
    ielts_Exam = models.ForeignKey("Master.ielts_Exam" , on_delete=models.CASCADE , blank=True , null=True)
    PTE_Exam = models.ForeignKey("Master.PTE_Exam" , on_delete=models.CASCADE , blank=True , null=True)
    Duolingo_Exam = models.ForeignKey("Master.Duolingo_Exam" , on_delete=models.CASCADE , blank=True , null=True)
    Gre_Exam = models.ForeignKey("Master.Gre_Exam" , on_delete=models.CASCADE , blank=True , null=True)
    Gmat_Exam = models.ForeignKey("Master.Gmat_Exam" , on_delete=models.CASCADE , blank=True , null=True)
    Remark = models.TextField(blank=True , verbose_name="Notes" , null=True)
    Active = models.BooleanField()
    newsletter = models.FileField(upload_to='newsletter/' , blank=True , verbose_name="Newsletters" , null=True)
    assigned_users = models.ForeignKey(get_user_model() , on_delete=models.CASCADE , default="" , blank=True ,
                                       null=True)

    def __str__(self):
        return self.univ_name
        
        
        
        
        
        
        
        
        
        
        
        
class campus(models.Model):
    campus_university = models.ForeignKey(university, on_delete=models.CASCADE,blank=True , null=True)
    campus_name = models.CharField(max_length=100,blank=True , null=True)
    campus_location = models.CharField(max_length=100,blank=True , null=True)
    campus_address = models.CharField(max_length=100,blank=True , null=True)
    campus_phone = models.CharField(max_length=10,blank=True , null=True)
    campus_email = models.EmailField(max_length=254,blank=True , null=True)
    campus_website = models.URLField(blank=True , null=True)

    def __str__(self):
        return self.campus_name


class Course(models.Model):
    country = models.ForeignKey(country , on_delete=models.CASCADE , blank=True , null=True)
    university = models.ForeignKey(university , on_delete=models.CASCADE , blank=True , null=True)
    

    course_name = models.CharField(max_length=100 , blank=True , null=True)
    course_levels = models.ForeignKey(course_levels , on_delete=models.CASCADE , blank=True , null=True)
    intake = models.ManyToManyField(intake , blank=True , null=True)
    website_url = models.URLField(blank=True , null=True)
    specialisation_tag = TagField(blank=True , null=True)
    documents_required = models.ManyToManyField(documents_required , blank=True , null=True)
    tenth_std_percentage_requirement = models.ForeignKey("Master.tenth_std_percentage_requirement" ,
                                                         on_delete=models.CASCADE , blank=True , null=True)
    twelfth_std_percentage_requirement = models.ForeignKey("Master.twelfth_std_percentage_requirement" ,
                                                           on_delete=models.CASCADE , blank=True , null=True)
    bachelor_requirement = models.ForeignKey("Master.bachelor_requirement" , on_delete=models.CASCADE , blank=True ,
                                             null=True)
    masters_requirement = models.ForeignKey("Master.masters_requirement" , on_delete=models.CASCADE , blank=True ,
                                            null=True)
    Toefl_Exam = models.ForeignKey("Master.Toefl_Exam" , on_delete=models.CASCADE , blank=True , null=True)
    ielts_Exam = models.ForeignKey("Master.ielts_Exam" , on_delete=models.CASCADE , blank=True , null=True)
    PTE_Exam = models.ForeignKey("Master.PTE_Exam" , on_delete=models.CASCADE , blank=True , null=True)
    Duolingo_Exam = models.ForeignKey("Master.Duolingo_Exam" , on_delete=models.CASCADE , blank=True , null=True)
    Gre_Exam = models.ForeignKey("Master.Gre_Exam" , on_delete=models.CASCADE , blank=True , null=True)
    Gmat_Exam = models.ForeignKey("Master.Gmat_Exam" , on_delete=models.CASCADE , blank=True , null=True)
    other_exam = models.CharField(max_length=100 , blank=True , null=True)
    Application_deadline = models.DateField(blank=True , null=True)
    Application_fee = models.FloatField(blank=True , null=True)
    Application_fee_currency = models.CharField(max_length=10 , blank=True , null=True)
    Yearly_Tuition_fee = models.FloatField(blank=True , null=True)
    Backlogs_allowed = models.IntegerField(blank=True , null=True)
    Remark = models.TextField(blank=True , verbose_name="Notes" , null=True)
    Active = models.BooleanField()
    Univ_Campus = models.ManyToManyField(campus , blank=True , null=True)

    def __str__(self):
        return f"{self.course_name} - {self.university}"
        
        
        
        
        
        
        


# add a field to class Rejection_Reason which is a file field to upload the refusal letter
