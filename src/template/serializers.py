from dataclasses import field
from rest_framework import serializers
from src.template.models import Templates

class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Templates
        fields = "__all__"