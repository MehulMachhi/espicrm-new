# Create your views here.
from rest_framework import generics
from .serializers import LeadSerializer
from .models import Lead

class LeadView(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer