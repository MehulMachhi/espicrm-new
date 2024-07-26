# Create your models here.
from django.contrib.auth import get_user_model
from django.db import models


class FollowupStatus(models.Model):
    status_name = models.CharField(max_length=100)

    def __str__(self):
        return self.status_name


class Task(models.Model):
    task_name = models.CharField(max_length=100)
    task_description = models.TextField()
    assigned_to = models.ForeignKey(get_user_model() , on_delete=models.CASCADE)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task_name


class Followups(models.Model):
    followup_date = models.DateField(auto_now_add=True)
    followup_status = models.ForeignKey(FollowupStatus , on_delete=models.CASCADE)
    notes = models.TextField()
    tasks = models.ManyToManyField(Task , blank=True , related_name='followups')
    assigned_to = models.ForeignKey(get_user_model() , on_delete=models.CASCADE)
    next_followup_date = models.DateField(blank=True , null=True)

    def __str__(self):
        return f"Followup for {self.followup_status} on {self.followup_date}"
