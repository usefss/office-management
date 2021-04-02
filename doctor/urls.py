from django.urls import path

from .views import SetDoctorVisitAPI, DoctorsVisitors, ChangeOfficeInfo, GetComments

urlpatterns = [
    path('set-doctor-visit/', SetDoctorVisitAPI.as_view()),
    path('get-visitors/', DoctorsVisitors.as_view()),
    path('change-office-info/', ChangeOfficeInfo.as_view()),
    path('get-comments/', GetComments.as_view()),
]
