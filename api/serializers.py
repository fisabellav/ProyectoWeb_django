from dataclasses import field
from rest_framework import serializers
from crud.models import *

class SpecializationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    
    class Meta:
        model = Specialization
        fields = (
            'id','specialization','created_at','updated_at'
        )
    
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = (
            'subject','specialization','semester','created_at','updated_at'
        )