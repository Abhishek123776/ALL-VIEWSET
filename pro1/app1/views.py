from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from . models import Contact,Educationdetail,Familydetails,Partnerprefarencedetails
from . serializers import ContactSerializer,EducationdetailSerializer,FamilydetailsSerializer,PartnerprefarencedetailsSerializer
# Create your views here.

class ContactViewset(viewsets.ViewSet):
    def create(self,request):
        serializer=ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)

    def list(self,request):
        objs=Contact.objects.all()
        serializer=ContactSerializer(objs,many=True)
        return Response(data=serializer.data)

    def retrieve(self,request,pk=None):
        obj=get_object_or_404(Contact,id=pk)
        serializer=ContactSerializer(obj)
        return Response(data=serializer.data)
    
    def update(self,request,pk=None):
        obj=get_object_or_404(Contact,id=pk)
        serializer=ContactSerializer(instance=obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
    
    def partial_update(self,request,pk=None):
        obj=get_object_or_404(Contact,id=pk)
        serializer=ContactSerializer(instance=obj,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
    
    def destroy(self,request,pk=None):
        obj=get_object_or_404(Contact,id=pk)
        obj.delete()
        return Response(data={"msg":'DATA DELETED SUCCESSFULY'})

class EducationdetailViewset(viewsets.ViewSet):
    def create(self,request):
        serializer=EducationdetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)

    def list(self,request):
        objs=Educationdetail.objects.all()
        serializer=EducationdetailSerializer(objs,many=True)
        return Response(data=serializer.data)

    def retrieve(self,request,pk=None):
        obj=get_object_or_404(Educationdetail,id=pk)
        serializer=EducationdetailSerializer(obj)
        return Response(data=serializer.data)
    
    def update(self,request,pk=None):
        obj=get_object_or_404(Educationdetail,id=pk)
        serializer=EducationdetailSerializer(instance=obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
    
    def partial_update(self,request,pk=None):
        obj=get_object_or_404(Educationdetail,id=pk)
        serializer=EducationdetailSerializer(instance=obj,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
    
    def destroy(self,request,pk=None):
        obj=get_object_or_404(Educationdetail,id=pk)
        obj.delete()
        return Response(data={"msg":'DATA DELETED SUCCESSFULY'})
    
class FamilydetailsViewset(viewsets.ViewSet):
    def create(self,request):
        serializer=FamilydetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)

    def list(self,request):
        objs=Familydetails.objects.all()
        serializer=FamilydetailsSerializer(objs,many=True)
        return Response(data=serializer.data)

    def retrieve(self,request,pk=None):
        obj=get_object_or_404(Familydetails,id=pk)
        serializer=FamilydetailsSerializer(obj)
        return Response(data=serializer.data)
    
    def update(self,request,pk=None):
        obj=get_object_or_404(Familydetails,id=pk)
        serializer=FamilydetailsSerializer(instance=obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
    
    def partial_update(self,request,pk=None):
        obj=get_object_or_404(Familydetails,id=pk)
        serializer=FamilydetailsSerializer(instance=obj,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
    
    def destroy(self,request,pk=None):
        obj=get_object_or_404(Familydetails,id=pk)
        obj.delete()
        return Response(data={"msg":'DATA DELETED SUCCESSFULY'})
    
class PartnerprefarencedetailsViewset(viewsets.ViewSet):
    def create(self,request):
        serializer=PartnerprefarencedetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)

    def list(self,request):
        objs=Partnerprefarencedetails.objects.all()
        serializer=PartnerprefarencedetailsSerializer(objs,many=True)
        return Response(data=serializer.data)

    def retrieve(self,request,pk=None):
        obj=get_object_or_404(Partnerprefarencedetails,id=pk)
        serializer=PartnerprefarencedetailsSerializer(obj)
        return Response(data=serializer.data)
    
    def update(self,request,pk=None):
        obj=get_object_or_404(Partnerprefarencedetails,id=pk)
        serializer=PartnerprefarencedetailsSerializer(instance=obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
    
    def partial_update(self,request,pk=None):
        obj=get_object_or_404(Partnerprefarencedetails,id=pk)
        serializer=PartnerprefarencedetailsSerializer(instance=obj,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
    
    def destroy(self,request,pk=None):
        obj=get_object_or_404(Partnerprefarencedetails,id=pk)
        obj.delete()
        return Response(data={"msg":'DATA DELETED SUCCESSFULY'})