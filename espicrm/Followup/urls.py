from django.urls import path
from .views import FollowUpStatuView, TaskListView

urlpatterns = [
    path('followupstatus/', FollowUpStatuView.as_view()),
    path('task-list-view/', TaskListView.as_view()),
]
