from rest_framework import serializers
from .models import Paragraph,ParagraphDTO

class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = '__all__'

class ParagraphDTOSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParagraphDTO
        fields = '__all__'
