from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status

from rest_framework.mixins import (
    CreateModelMixin, DestroyModelMixin, ListModelMixin,
    RetrieveModelMixin, UpdateModelMixin,
)

from drf_spectacular.utils import extend_schema
from .serializers import IdOptionalSerializer, IdSerializer


class BaseAPI(GenericAPIView, CreateModelMixin, DestroyModelMixin,
              ListModelMixin, RetrieveModelMixin, UpdateModelMixin):

    def get_queryset(self):
        queryset = super(BaseAPI, self).get_queryset()
        return queryset.filter(
            patient_id=self.request.user.user_id
        )

    def dispatch(self, request, *args, **kwargs):
        for key in request.GET:
            kwargs[key] = request.GET.get(key, None)

        return super(BaseAPI, self).dispatch(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['patient_id'] = self.request.user.user_id
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @extend_schema(
        parameters=[IdOptionalSerializer, ],
    )
    def get(self, request, *args, **kwargs):
        if self.kwargs.get(self.lookup_field, None):
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    @extend_schema(
        parameters=[IdSerializer, ],
    )
    def patch(self, request, *args, **kwargs):
        if self.kwargs.get(self.lookup_field, None):
            return self.partial_update(request, *args, **kwargs)
        else:
            raise ValidationError(
                'expected to be called with ' + str(self.lookup_field) + '!')

    @extend_schema(
        parameters=[IdSerializer, ],
    )
    def delete(self, request, *args, **kwargs):
        if self.kwargs.get(self.lookup_field, None):
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError(
                'expected to be called with ' + str(self.lookup_field))
