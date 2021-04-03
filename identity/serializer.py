from rest_framework import serializers


class signUpUserSerializer(serializers.Serializer):
    name = serializers.CharField()
    phone_number = serializers.CharField()
    email = serializers.CharField()

class SearchDoctorSerializer(serializers.Serializer):
    name = serializers.CharField()
    city = serializers.CharField()
    expertise = serializers.CharField()
    degree = serializers.CharField()

class PatientInfoChangeSerializer(serializers.Serializer):
    name = serializers.CharField()
    phone_number = serializers.CharField()











