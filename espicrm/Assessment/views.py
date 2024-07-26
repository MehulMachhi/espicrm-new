# Create your views here.
from rest_framework import viewsets

from .models import assessment
from .serializers import AssessmentSerializer


class AssessmentViewSet(viewsets.ModelViewSet):
    queryset = assessment.objects.all()
    serializer_class = AssessmentSerializer
