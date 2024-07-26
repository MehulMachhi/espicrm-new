from rest_framework import viewsets

from .models import enquiry
from .serializers import EnquirySerializer


class EnquiryViewSet(viewsets.ModelViewSet):
    queryset = enquiry.objects.all()
    serializer_class = EnquirySerializer
