from django.urls import path
from .views import (
    PatientVisitingAPI,
    DoctorCommentAPI,
    FavoriteDoctorAPI
)

urlpatterns = [
    path('patient-visiting/', PatientVisitingAPI.as_view()),
    path('doctor-comment/', DoctorCommentAPI.as_view()),
    path('favorite-doctor/', FavoriteDoctorAPI.as_view()),
]
