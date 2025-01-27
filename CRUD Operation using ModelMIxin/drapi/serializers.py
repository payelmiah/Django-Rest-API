from rest_framework import serializers
from .models import Aiquest

#Serializer class (model serializer)
class AiquestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aiquest # model Aiquest is used into models.py
        fields = ['id' ,'teacher_name', 'course_name', 'course_douration', 'seat'] #fields of model Aiquest


"""
#This is a basic serializer class used for better understanding

class AiquestSerializer(serializers.Serializer):  #Serializer class
    teacher_name = serializers.CharField(max_length=100)
    course_name = serializers.CharField(max_length=100)
    course_douration = serializers.IntegerField()
    seat = serializers.IntegerField()
    

    #deserialization create method
    def create(self, validated_data):
        return Aiquest.objects.create(**validated_data) #validated_data is a dictionary of deserialized data
    
    #deserialization update method
    def update(self, instance, validated_data):
        instance.teacher_name = validated_data.get('teacher_name', instance.teacher_name)
        instance.course_name = validated_data.get('course_name', instance.course_name)
        instance.course_douration = validated_data.get('course_douration', instance.course_douration)
        instance.seat = validated_data.get('seat', instance.seat)
        instance.save()
        return instance
"""