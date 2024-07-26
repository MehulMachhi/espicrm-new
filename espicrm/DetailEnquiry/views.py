# Create your views here.
from rest_framework import viewsets

from .models import Detail_Enquiry
from .serializers import DetailEnquirySerializer


class DetailEnquiryViewSet(viewsets.ModelViewSet):
    queryset = Detail_Enquiry.objects.all()
    serializer_class = DetailEnquirySerializer
