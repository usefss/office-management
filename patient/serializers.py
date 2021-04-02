from rest_framework import serializers
from .models import PatientVisiting, DoctorComment, FavoriteDoctor


class DoctorCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorComment
        exclude = ['patient_id', ]


class PatientVisitingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientVisiting
        exclude = ['patient_id', ]


class FavoriteDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteDoctor
        exclude = ['patient_id', ]


class IdOptionalSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=32, required=False)


class IdSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=32)
