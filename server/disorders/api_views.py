from rest_framework.generics import ListAPIView
from .serializers import DisorderSerializer, SymptomsSerializer
from .models import Disorders
from .models import Symptoms
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination


class SymptomsPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 5


class DisorderList(ListAPIView):
    queryset = Disorders.objects.all()
    serializer_class = DisorderSerializer
    fields = ('name')
    pagination_class = SymptomsPagination

    def get_queryset(self):
        name = self.request.query_params.get('name', None)
        if name is None:
            return super().get_queryset()
        queryset = Disorders.objects.all()
        symptom_name = queryset.filter(name=name)
        queryset = symptom_name
        return queryset


class FilterSymptoms(ListAPIView):
    queryset = Symptoms.objects.all()


class SymptomsList(ListAPIView):
    queryset = Symptoms.objects.all()
    serializer_class = SymptomsSerializer
    filter_backends = (DjangoFilterBackend,)
    fields = ('name')
    pagination_class = SymptomsPagination

    def get_queryset(self):
        name = self.request.query_params.get('name', None)
        if name is None:
            return super().get_queryset()
        queryset = Symptoms.objects.all()
        symptom_name = queryset.filter(name=name)
        queryset = symptom_name
        return queryset
