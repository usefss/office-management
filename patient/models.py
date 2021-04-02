from django.db import models


class PatientVisiting(models.Model):
    visiting_date_id = models.CharField(max_length=32)
    patient_id = models.CharField(max_length=32, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)


class DoctorComment(models.Model):
    comment = models.CharField(max_length=256)
    doctor_id = models.CharField(max_length=32)
    patient_id = models.CharField(max_length=32, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)


class FavoriteDoctor(models.Model):
    doctor_id = models.CharField(max_length=32)
    patient_id = models.CharField(max_length=32, null=True, blank=True)
