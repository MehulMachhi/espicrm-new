from rest_framework import serializers

from .models import Detail_Enquiry


class DetailEnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail_Enquiry
        fields = '__all__'
