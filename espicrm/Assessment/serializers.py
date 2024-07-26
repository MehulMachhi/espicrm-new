from rest_framework import serializers

from .models import assessment


class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = assessment
        fields = '__all__'
