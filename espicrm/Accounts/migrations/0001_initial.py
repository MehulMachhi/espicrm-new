# Generated by Django 4.2.9 on 2024-03-27 19:39

import django.db.models.deletion
from django.db import migrations , models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('Master' , '0008_payment_mode_payment_status_payment_type') ,
    ]

    operations = [
        migrations.CreateModel(
            name='Payment' ,
            fields=[
                ('id' ,
                 models.BigAutoField(auto_created=True , primary_key=True , serialize=False , verbose_name='ID')) ,
                ('payment_id' , models.CharField(blank=True , max_length=100 , null=True)) ,
                ('payment_date' , models.DateField(auto_now_add=True)) ,
                ('payment_amount' , models.FloatField(blank=True , null=True)) ,
                ('payment_reference' , models.CharField(blank=True , max_length=100 , null=True)) ,
                ('payment_remarks' , models.TextField(blank=True , null=True)) ,
                ('payment_document' , models.FileField(blank=True , upload_to='documents/')) ,
                ('Payment_For' , models.ForeignKey(blank=True , on_delete=django.db.models.deletion.CASCADE ,
                                                   to='Master.available_services')) ,
                ('Payment_Type' , models.ForeignKey(blank=True , on_delete=django.db.models.deletion.CASCADE ,
                                                    to='Master.payment_type')) ,
                ('payment_mode' , models.ForeignKey(blank=True , on_delete=django.db.models.deletion.CASCADE ,
                                                    to='Master.payment_mode')) ,
                ('payment_status' , models.ForeignKey(blank=True , on_delete=django.db.models.deletion.CASCADE ,
                                                      to='Master.payment_status')) ,
            ] ,
        ) ,
    ]
