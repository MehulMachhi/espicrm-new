from django.contrib.auth import get_user_model
from django.db import models
from django_countries.fields import CountryField
from smart_selects.db_fields import ChainedForeignKey
from Master.models import university
from Master.models import course_levels
from Master.models import Course
from Master.models import country




class enquiry(models.Model):
    # Personal Info
    student_First_Name = models.CharField(max_length=100)
    student_Last_Name = models.CharField(max_length=100)
    student_passport = models.CharField(max_length=100)
    Source_Enquiry = models.ForeignKey('Master.Enquiry_Source', on_delete=models.CASCADE, blank=True, default='Website')

    # Contact Info
    student_phone = models.CharField(unique=True, blank=True, max_length=10)
    alternate_phone = models.CharField(max_length=10)
    student_email = models.EmailField()
    student_address = models.TextField()
    student_country = CountryField(blank_label="(select country)", default="IN")
    student_state = models.CharField(max_length=100)
    student_city = models.CharField(max_length=100)
    student_zip = models.CharField(max_length=10)

    # Education Info
    current_education = models.ForeignKey('Master.Current_Education', on_delete=models.CASCADE)

    # Enquiry Info
    country_interested = models.ManyToManyField(country,)
    university_interested = ChainedForeignKey(
        university,
        chained_field="country_interested",
        chained_model_field="country",
        show_all=False,
        auto_choose=True,
        sort=True,
        on_delete=models.CASCADE,
        verbose_name="Interested University"
    )
    level_applying_for = ChainedForeignKey(
        course_levels,
        chained_field='university_interested',
        chained_model_field="university",
        show_all=False,
        auto_choose=True,
        sort=True,
        on_delete=models.CASCADE,
        verbose_name="Applying for Level"
    )
    course_interested = ChainedForeignKey(
        Course,
        chained_field="level_applying_for",
        chained_model_field="course_levels",
        show_all=False,
        auto_choose=True,
        sort=True,
        on_delete=models.CASCADE,
        verbose_name="Interested Course"
    )
    intake_interested = models.ForeignKey('Master.Intake', on_delete=models.CASCADE)
    Interested_Services = models.ManyToManyField('Master.Available_Services', blank=True, related_name="Interested_Services", default='Counselling')

    # For Counsellor
    assigned_users = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default="")
    enquiry_status = models.ForeignKey('Master.Enquiry_Status', on_delete=models.CASCADE)
    notes = models.TextField()
    followup_create = models.ForeignKey('Followup.Followups', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.student_First_Name} {self.student_Last_Name}"
