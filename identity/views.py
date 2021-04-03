"""
    API services needed here are:
        - signup users |A: anybody
        * access control management
        * users are patients or doctors
        * signup doctor needs doctor_number, doctor_phone

        - get doctors list filters by city, expertise, degree |A: anybody
        - patient can edit self information like name, family, phone
"""
from random import randint

from django.utils import timezone
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from doctor.views import GetComments
from identity.serializer import (
    SearchDoctorSerializer, signUpUserSerializer, PatientInfoChangeSerializer,
    signUpDoctorSerializer,
)


class SignUpUser(APIView):
    @extend_schema(
        request=signUpUserSerializer,
    )
    def post(self, request):
        """
            MOCKED API
            request:
            [
                {
                    'name' : text,
                    'phone_number' : text,
                    'email' : text,
                },
            ]
            response:
            [
                {
                    'status_message' : text,
                    'created_at' : DateTime,
                }
            ]
        """
        param_serializer = signUpUserSerializer(data=request.data)
        param_serializer.is_valid(raise_exception=True)
        return Response([
            {
                'id':  randint(1, 100),
                'created_at': timezone.now(),
            }
        ])


class SignUpDoctor(APIView):
    @extend_schema(
        request=signUpDoctorSerializer,
    )
    def post(self, request):
        """
            MOCKED API
            request:
            [
                {
                    'name' : text,
                    'phone_number' : text,
                    'email' : text,
                },
            ]
            response:
            [
                {
                    'status_message' : text,
                    'created_at' : DateTime,
                }
            ]
        """
        param_serializer = signUpDoctorSerializer(data=request.data)
        param_serializer.is_valid(raise_exception=True)
        return Response([
            {
                'id':  randint(1, 100),
                'created_at': timezone.now(),
            }
        ])


class DoctorSearch(APIView):
    @extend_schema(
        parameters=[SearchDoctorSerializer],
    )
    def get(self, request):
        """
            MOCKED API
            request:
            [
                {
                    'name' : text,
                    'city' : text,
                    'expertise' : text,
                    'degree' : text,
                },
            ]
            response:
            [
                {
                    'name' : text,
                },
            ]
        """
        return Response([
            {
                'id': randint(1, 100),
                'name': 'doctor' + str(randint(1, 100)),
            }
        ])


class PatientInfoChange(APIView):
    @extend_schema(
        request=PatientInfoChangeSerializer,
    )
    def patch(self, request):
        """
            MOCKED API
            request:
            {
                'name': text,
                'phone_number': int,
            }
            response: gets a json object of inserted information
            {
                'created_at' : text,
            }
        """
        serializer = PatientInfoChangeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(
            {
                **serializer.data,
                'updated_at': timezone.now(),
                'id': randint(1, 100),
            })
