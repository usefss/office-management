from rest_framework import serializers

from identity.models import User, SearchDoctor, PatientInfo


class signUpUserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = '__all__'

class SearchDoctorSerializer(serializers.Serializer):
    class Meta:
        model = SearchDoctor
        fields = '__all__'

class ChangePatientInfoSerializer(serializers.Serializer):
    class Meta:
        model = PatientInfo
        fields = '__all__'











