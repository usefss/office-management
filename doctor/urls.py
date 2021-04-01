from django.urls import path

from .views import SetDoctorVisitAPI, DoctorsVisitors

urlpatterns = [
    path('set-doctor-visit/', SetDoctorVisitAPI.as_view()),
    path('get-visitors/', DoctorsVisitors.as_view()),
]
