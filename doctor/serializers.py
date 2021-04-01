from rest_framework import serializers


class SetDoctorVisitSerializer(serializers.Serializer):
    date = serializers.DateField()
    from_time = serializers.TimeField()
    to_time = serializers.TimeField()


class GetVisitorsParams(serializers.Serializer):
    date = serializers.DateField()
