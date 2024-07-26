# Create your views here.
from .serializers import FollowupStatusSerializer, Taskserializer
from .models import FollowupStatus, Task
from rest_framework import generics, status
from rest_framework import authentication


class FollowUpStatuView(generics.ListCreateAPIView):
    serializer_class = FollowupStatusSerializer
    queryset = FollowupStatus.objects.all()


class TaskListView(generics.ListCreateAPIView):
    serializer_class = Taskserializer
    queryset = Task.objects.all()

