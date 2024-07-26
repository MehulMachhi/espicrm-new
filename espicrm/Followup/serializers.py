from rest_framework import serializers
from .models import FollowupStatus, Task

class FollowupStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowupStatus
        fields = "__all__"

class Taskserializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
