from rest_framework import serializers
from src.style import Style
from src.template.serializers import TemplateSerializer

class StyleSerializer(serializers.ModelSerializer):
    templates = TemplateSerializer(many=True)
    class Meta:
        model = Style
        fields = '__all__'
        read_only_fields= ['created']