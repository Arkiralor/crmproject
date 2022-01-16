from rest_framework import serializers
from .models import Questionare

# Create your serializers here:

class QuestionareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionare
        # fields = ['fname', 'lname', 'email', 'phone', 'course']
        fields = '__all__'

class QuestionareSerializerAll(serializers.ModelSerializer):
    class Meta:
        model = Questionare
        fields = '__all__'