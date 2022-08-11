from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from src.users.permissions import IsUserOrReadOnly
from rest_framework import permissions

from src.files import serializers

# Create your views here.
class ListTemplate(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly]

    