from rest_framework import serializers


class SetDoctorVisitSerializer(serializers.Serializer):
    date = serializers.DateField()
    from_time = serializers.TimeField()
    to_time = serializers.TimeField()


class GetVisitorsParams(serializers.Serializer):
    date = serializers.DateField()


class OfficeInfo(serializers.Serializer):
    address = serializers.CharField()
    phone_number = serializers.IntegerField()


class GetComments(serializers.Serializer):
    # visitor_id = serializers.IntegerField()
    comment = serializers.CharField()
    id = serializers.IntegerField()
    created_at = serializers.DateTimeField()


