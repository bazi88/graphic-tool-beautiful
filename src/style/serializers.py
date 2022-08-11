from rest_framework import serializers
from src.style import Style

class StyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Style
        fields = '__all__'
        read_only_fields= ['created']