"""
    API services needed here are:
        - signup users |A: anybody
        * access control management
        * users are patients or doctors
        * signup doctor needs doctor_number, doctor_phone

        - get doctors list filters by city, expertise, degree |A: anybody
        - patient can edit self information like name, family, phone
"""
class SignUpUser(APIView):
    @extend_schema(
    )
    def get(self, request):
        """
            MOCKED API
            request: empty
            response:
            [
                {
                    # vistor_id: FakeInt,
                    comment: text,
                    id: FakeInt,
                    created_at: DateTime,
                },
                ...
            ]
        """
        param_serializer = GetComments(request.GET)
        param_serializer.is_valid(raise_exception=True)
        return Response([
        {
            'comment':  "I don't Know",
            'id': randint(1, 100),
            'created_at': timezone.now(),
        }
        ])









# class SignUserAPI(BaseAPI):
#     lookup_field = 'id'
#     queryset = SignupUser.objects.all()
#     serializer_class = SignUpUserSerializer
#
#
# class SearchDoctorAPI(BaseAPI):
#     lookup_field = 'id'
#     queryset = SearchDoctor.objects.all()
#     serializer_class = SearchDoctorSerializer
#
#
# class ChangePatientInfoAPI(BaseAPI):
#     lookup_field = 'id'
#     queryset = ChangePatientInfo.objects.all()
#     serializer_class = ChangePatientInfoSerializer