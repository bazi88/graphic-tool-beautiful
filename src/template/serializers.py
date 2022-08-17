from dataclasses import field
from rest_framework import serializers
from src.template.models import Templates

class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Templates
        fields = ('created','name_template','updated', 'type_template', 'style', 'name')
