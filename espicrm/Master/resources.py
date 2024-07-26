from django.contrib.auth import get_user_model
from import_export import resources , fields
from import_export.widgets import ForeignKeyWidget , ManyToManyWidget

from .models import Course , country , university , course_levels , intake , campus , documents_required , \
    tenth_std_percentage_requirement , twelfth_std_percentage_requirement , bachelor_requirement , masters_requirement , \
    Toefl_Exam , ielts_Exam , PTE_Exam , Duolingo_Exam , Gre_Exam , Gmat_Exam


class CourseResource(resources.ModelResource):
    country = fields.Field(column_name='country' , attribute='country' ,
                           widget=ForeignKeyWidget(country , 'country_name'))
    university = fields.Field(column_name='university' , attribute='university' ,
                              widget=ForeignKeyWidget(university , 'name'))
    course_levels = fields.Field(column_name='course_levels' , attribute='course_levels' ,
                                 widget=ForeignKeyWidget(course_levels , 'level_name'))
    intake = fields.Field(column_name='intake' , attribute='intake' ,
                          widget=ManyToManyWidget(intake , separator=', ' , field='intake_Name'))
    Campus = fields.Field(column_name='Campus' , attribute='Campus' ,
                          widget=ManyToManyWidget(campus , separator=', ' , field='campus_name'))
    documents_required = fields.Field(column_name='documents_required' , attribute='documents_required' ,
                                      widget=ManyToManyWidget(documents_required , separator=', ' ,
                                                              field='document_name'))
    tenth_std_percentage_requirement = fields.Field(column_name='tenth_std_percentage_requirement' ,
                                                    attribute='tenth_std_percentage_requirement' ,
                                                    widget=ForeignKeyWidget(tenth_std_percentage_requirement ,
                                                                            'requirement_name'))
    twelfth_std_percentage_requirement = fields.Field(column_name='twelfth_std_percentage_requirement' ,
                                                      attribute='twelfth_std_percentage_requirement' ,
                                                      widget=ForeignKeyWidget(twelfth_std_percentage_requirement ,
                                                                              'requirement_name'))
    bachelor_requirement = fields.Field(column_name='bachelor_requirement' , attribute='bachelor_requirement' ,
                                        widget=ForeignKeyWidget(bachelor_requirement , 'requirement_name'))
    masters_requirement = fields.Field(column_name='masters_requirement' , attribute='masters_requirement' ,
                                       widget=ForeignKeyWidget(masters_requirement , 'requirement_name'))
    Toefl_Exam = fields.Field(column_name='Toefl_Exam' , attribute='Toefl_Exam' ,
                              widget=ForeignKeyWidget(Toefl_Exam , 'exam_name'))
    ielts_Exam = fields.Field(column_name='ielts_Exam' , attribute='ielts_Exam' ,
                              widget=ForeignKeyWidget(ielts_Exam , 'exam_name'))
    PTE_Exam = fields.Field(column_name='PTE_Exam' , attribute='PTE_Exam' ,
                            widget=ForeignKeyWidget(PTE_Exam , 'exam_name'))
    Duolingo_Exam = fields.Field(column_name='Duolingo_Exam' , attribute='Duolingo_Exam' ,
                                 widget=ForeignKeyWidget(Duolingo_Exam , 'exam_name'))
    Gre_Exam = fields.Field(column_name='Gre_Exam' , attribute='Gre_Exam' ,
                            widget=ForeignKeyWidget(Gre_Exam , 'exam_name'))
    Gmat_Exam = fields.Field(column_name='Gmat_Exam' , attribute='Gmat_Exam' ,
                             widget=ForeignKeyWidget(Gmat_Exam , 'exam_name'))

    class Meta:
        model = Course
        fields = (
        'id' , 'country' , 'university' , 'course_name' , 'course_levels' , 'intake' , 'Campus' , 'website_url' ,
        'specialisation_tag' , 'documents_required' , 'tenth_std_percentage_requirement' ,
        'twelfth_std_percentage_requirement' , 'bachelor_requirement' , 'masters_requirement' , 'Toefl_Exam' ,
        'ielts_Exam' , 'PTE_Exam' , 'Duolingo_Exam' , 'Gre_Exam' , 'Gmat_Exam' , 'other_exam' , 'Application_deadline' ,
        'Application_fee' , 'Application_fee_currency' , 'Yearly_Tuition_fee' , 'Backlogs_allowed' , 'Remark' ,
        'Active')


class UniversityResource(resources.ModelResource):
    country = fields.Field(column_name='country' , attribute='country' ,
                           widget=ForeignKeyWidget(country , 'country_name'))
    Univ_Campus = fields.Field(column_name='Univ_Campus' , attribute='Univ_Campus' ,
                               widget=ManyToManyWidget(campus , separator=', ' , field='campus_name'))
    levels = fields.Field(column_name='levels' , attribute='levels' ,
                          widget=ManyToManyWidget(course_levels , separator=', ' , field='level_name'))
    assigned_users = fields.Field(column_name='assigned_users' , attribute='assigned_users' ,
                                  widget=ForeignKeyWidget(get_user_model() , 'username'))

    class Meta:
        model = university
        fields = (
            'id' , 'univ_name' , 'country' , 'Univ_Campus' , 'levels' , 'univ_desc' , 'deadline' , 'moi_accepted' ,
            'Application_form' , 'Application_form_link' , 'Application_fee' , 'Admission_Requirements' ,
            'Backlogs_allowed' ,
            'univ_logo' , 'univ_phone' , 'univ_email' , 'univ_website' , 'tenth_std_percentage_requirement' ,
            'twelfth_std_percentage_requirement' , 'bachelor_requirement' , 'masters_requirement' , 'Toefl_Exam' ,
            'ielts_Exam' ,
            'PTE_Exam' , 'Duolingo_Exam' , 'Gre_Exam' , 'Gmat_Exam' , 'Remark' , 'Active' , 'newsletter' ,
            'assigned_users'
        )
