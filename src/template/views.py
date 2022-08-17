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
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.
# class ListTemplate(APIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly]

response_schema_dict = {
    "200": openapi.Response(
        description="custom 200 description",
        examples={
            "application/json": {
                "data": [
                    {
                        "name_template": "",
                        "type_template": "",
                        "style": "",
                        "name": ""
                    }
                ],
                "status": "200 OK"
            }
        }
    ),
    "205": openapi.Response(
        description="custom 205 description",
        examples={
            "application/json": {
                "205_key1": "205_value_1",
                "205_key2": "205_value_2",
            }
        }
    ),
}
class TemplateView(APIView):
    """
    Get and post a template - Templates
    """
    def get(self, request, *args, **kwargs):
        template =  Templates.objects.all()
        serializer = TemplateSerializer(template, many=True)
        return JsonResponse({"data": serializer.data, "status": status.HTTP_200_OK})

    @swagger_auto_schema(responses=response_schema_dict, request_body=TemplateSerializer)
    def post(self, request, *args, **kwargs):
        serializer = TemplateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"data": serializer.data, "status": status.HTTP_201_CREATED})
        return JsonResponse({"error": serializer.error, "status": status.HTTP_400_BAD_REQUEST})
    
class TemplateDetailView(APIView):
    """
    Get details of a template and update, delete - Templates
    """
    def get_object(self,pk):
        try:
            Templates.objects.get(pk=pk)
        except Templates.DoesNotExist:
            raise Http404

    def get(self, request,pk ,format=None):
        template = self.get_object(pk=pk)
        serializer = TemplateSerializer(template)
        return JsonResponse({"data": serializer.data,  "status": status.HTTP_200_OK})

    def put(self, request, pk, format=None):
        template = self.get_object(pk=pk)
        serializer = TemplateSerializer(template, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"data": serializer.data, "status":status.HTTP_202_ACCEPTED})
        return JsonResponse({"error": serializer.error, "status": status.HTTP_400_BAD_REQUEST})
        
    def delete(self, request, pk, format=None):
        template = self.get_object(pk=pk)
        template.delete()
        return JsonResponse({"status": status.HTTP_204_NO_CONTENT})

