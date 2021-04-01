
"""
    API services needed here are:
        - doctor sets work days and times in every days
            A doctor has infinite days from signup or should he or she specify every day??
            1- infinite days: every day and its active time is a recourd in database and has a relation with 
                some other models so it is very hard to implement
            2- Doctor must clearify every day and time of visitations --> simple 
        - doctor can see visiting times set by patients
            A doctor has multiple patients for every day he is accepting visitors

        - change office information
        - see self comments
        * doctor has access over just self information not others
"""

from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response

from drf_spectacular.utils import extend_schema
from random import randint

from .serializers import SetDoctorVisitSerializer, GetVisitorsParams


class GetComments(APIView):
    @extend_schema()
    def get(self, request):
        """
            MOCKED API
            request: empty
            response: 
            [
                {
                    vistor_id: FakeInt,
                    comment: text,
                    id: FakeInt,
                    created_at: DateTime,
                },
                ...
            ]
        """
        pass


class OfficeInfo(APIView):
    @extend_schema()
    def patch(self, request):
        """
            MOCKED API
            request: 
            {
                address: text,
                phone_number: int,
                ...
            }
            response: get created data plus id and created_at
            {
                ...
            }
        """
        pass


class DoctorsVisitors(APIView):
    @extend_schema(
        parameters=[GetVisitorsParams],
    )
    def get(self, request):
        """
                MOCKED API
                request: doctor demands geting list of visitors for a day
                param: :date
                response: gets a list of visitors
                [
                    {
                        visitor_id or patient_id: FakeInt,
                        visiting_date_id: FakeInt, --> foreign key to the model that doctor creates when seting visiting dates
                        id: FakeInt, --> every record has a id
                    }
                ]
        """
        param_serializer = GetVisitorsParams(request.GET)
        param_serializer.is_valid(raise_exception=True)
        requested_date = param_serializer.validated_data['date']

        # here we get visitors by requested_date from database and serialize in a real API
        return Response([
            {
                'visitor_id': randint(1, 100),
                'visiting_date_id': randint(1, 100),
                'id': randint(1, 100),
            },
            {
                'visitor_id': randint(1, 100),
                'visiting_date_id': randint(1, 100),
                'id': randint(1, 100),
            },
        ])


class SetDoctorVisitAPI(APIView):
    @extend_schema(
        request=SetDoctorVisitSerializer,
    )
    def post(self, request):
        """
            MOCKED API
            request: doctor sends :day, :from_time, :to_time to create a recourd in database
            {
                date: DateTime,
                from_time: Time,
                to_time: Time,
            }
            response: gets a json object of inserted information
            {
                id: FakeInt,
                created_at: FakeDateTime,
                date: DateTime,
                from_time: Time,
                to_time: Time,
            }


            permissions: just doctor itself no other doctor
        """
        serializer = SetDoctorVisitSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # here serializer is valid and we save data to database in a real API
        return Response({
            **serializer.data,
            'id': randint(1, 1000),
            'created_at': timezone.now(),
        })
