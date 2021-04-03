from rest_framework import serializers


class signUpUserSerializer(serializers.Serializer):
    name = serializers.CharField()
    phone_number = serializers.CharField()
    email = serializers.CharField()


class signUpDoctorSerializer(signUpUserSerializer):
    doctor_phone = serializers.CharField()
    doctor_number = serializers.CharField()


class SearchDoctorSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    city = serializers.CharField(required=False)
    expertise = serializers.CharField(required=False)
    degree = serializers.CharField(required=False)


class PatientInfoChangeSerializer(serializers.Serializer):
    name = serializers.CharField()
    phone_number = serializers.CharField()
