from rest_framework import serializers
from MainApp.models import TemplateModel

class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemplateModel
        fields = ('Id')
