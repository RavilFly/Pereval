from rest_framework import serializers
from .models import PerevalAdded





class PerevalAddedSerializer(serializers.ModelSerializer):


    class Meta:
        model = PerevalAdded
        fields = '__all__'

    def create(self, validated_data):
        pereval_added = PerevalAdded.objects.create(**validated_data)
        return pereval_added