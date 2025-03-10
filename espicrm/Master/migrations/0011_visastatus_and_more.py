# Generated by Django 4.2.9 on 2024-06-26 06:32

import django.db.models.deletion
from django.db import migrations , models


class Migration(migrations.Migration):
    dependencies = [
        ('Master' , '0010_remove_substatus_reply_to_remarks') ,
    ]

    operations = [
        migrations.CreateModel(
            name='VisaStatus' ,
            fields=[
                ('id' ,
                 models.BigAutoField(auto_created=True , primary_key=True , serialize=False , verbose_name='ID')) ,
                ('status_name' , models.CharField(max_length=100 , unique=True , verbose_name='Status Name')) ,
            ] ,
        ) ,
        migrations.RemoveField(
            model_name='substatus' ,
            name='financial_documents_status' ,
        ) ,
        migrations.AddField(
            model_name='substatus' ,
            name='Admission_sub_sub' ,
            field=models.CharField(
                choices=[('Started' , 'Started') , ('Pending' , 'Pending') , ('Waiting' , 'Waiting')] , default=1 ,
                max_length=20 , verbose_name='Your Sub Status') ,
            preserve_default=False ,
        ) ,
        migrations.CreateModel(
            name='VisaSubStatus' ,
            fields=[
                ('id' ,
                 models.BigAutoField(auto_created=True , primary_key=True , serialize=False , verbose_name='ID')) ,
                ('visa_sub_status_name' , models.CharField(max_length=100 , verbose_name='Sub Status Name')) ,
                ('visa_sub_sub' , models.CharField(
                    choices=[('Started' , 'Started') , ('Pending' , 'Pending') , ('Waiting' , 'Waiting')] ,
                    max_length=20 , verbose_name='Your Visa Sub Status')) ,
                ('remarks' , models.TextField(blank=True , null=True , verbose_name='Remarks')) ,
                ('visa_status' ,
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE , related_name='substatuses' ,
                                   to='Master.visastatus')) ,
            ] ,
            options={
                'verbose_name': 'Sub Status' ,
                'verbose_name_plural': 'Sub Statuses' ,
            } ,
        ) ,
    ]
