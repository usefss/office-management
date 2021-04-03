from django.urls import path
from .views import SignUpUser, PatientInfoChange, DoctorSearch, SignUpDoctor

urlpatterns = [
    path('sign-up-user/', SignUpUser.as_view()),
    path('sign-up-doctor/', SignUpDoctor.as_view()),
    path('patient-info-change/', PatientInfoChange.as_view()),
    path('doctor-search/', DoctorSearch.as_view()),
]
