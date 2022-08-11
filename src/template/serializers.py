from rest_framework import serializers
from src.template import Template

class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = ['created',' name_template',' updated', 'type_template',' style']
        read_only_fields = ['created']