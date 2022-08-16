from re import template
from tempfile import tempdir
from django.shortcuts import render
from rest_framework.views import APIView
from src.users.permissions import IsUserOrReadOnly
from rest_framework import permissions, status
from src.template import serializers
from django.http import JsonResponse,Http404
from src.template.models import Templates
from django.forms.models import model_to_dict
from src.template.serializers import TemplateSerializer
# Create your views here.
# class ListTemplate(APIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly]

class TemplateView(APIView):
    def get(self, request, *args, **kwargs):
        template =  Templates.objects.all()
        serializer = TemplateSerializer(template, many=True)
        return JsonResponse({"data": serializer.data, "status": status.HTTP_200_OK})

    def post(self, request, *args, **kwargs):
        serializer = TemplateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"data": serializer.data, "status": status.HTTP_201_CREATED})
    
class TemplateDetailView(APIView):
    def get_object(self,pk):
        try:
            Templates.objects.get(pk=pk)
        except Templates.DoesNotExist:
            raise Http404

    def get(self, request,pk ,format=None):
        template = self.get_object(pk=pk)
        breakpoint()
        serializer = TemplateSerializer(template)
        return JsonResponse({"data": serializer.data,  "status": status.HTTP_200_OK})

    def put(self, request, pk, format=None):
        template = self.get_object(pk=pk)
        serializer = TemplateSerializer(template, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"data": serializer.data, "status":status.HTTP_202_ACCEPTED})

    def delete(self, request, pk, format=None):
        template = self.get_object(pk=pk)
        template.delete()
        return JsonResponse({"status": status.HTTP_204_NO_CONTENT})

