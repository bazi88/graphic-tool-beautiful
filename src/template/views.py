from django.shortcuts import render
from rest_framework.views import APIView
from src.users.permissions import IsUserOrReadOnly
from rest_framework import permissions
from src.template import serializers
from django.http import JsonResponse
from src.template.models import Templates
from django.forms.models import model_to_dict
# Create your views here.
# class ListTemplate(APIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly]

class ListView(APIView):
    def get(self, request, *args, **kwargs):
        template = list(Templates.objects.all().values())
        return JsonResponse({"data": template})

    def post(self, request, *args, **kwargs):
        templates = Templates.objects.create(
            name_template = request.data['name_template'],
            type_template= request.data['type_template'],
            style = request.data['style']
        )
        return JsonResponse({"data": model_to_dict(templates)})