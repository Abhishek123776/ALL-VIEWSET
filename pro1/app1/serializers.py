from rest_framework import serializers
from . models import Contact,Educationdetail,Familydetails,Partnerprefarencedetails

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields='__all__'

class EducationdetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Educationdetail
        fields='__all__'

class FamilydetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Familydetails
        fields='__all__'

class PartnerprefarencedetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Partnerprefarencedetails
        fields='__all__'