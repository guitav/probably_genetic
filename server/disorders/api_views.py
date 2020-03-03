from rest_framework.generics import ListAPIView
from .serializers import DisordersSerializer, SymptomsSerializer
from .models import Disorder
from .models import Symptom
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination


class ViewPagination(LimitOffsetPagination):
    """ 2 <= Pages < 5 for each view
    """
    default_limit = 2
    max_limit = 5


class DisorderList(ListAPIView):
    """ View disorders
        able to filter by name
    """
    queryset = Disorder.objects.all()
    serializer_class = DisordersSerializer
    fields = ('name')
    pagination_class = ViewPagination

    def get_queryset(self):
        name = self.request.query_params.get('name', None)
        if name is None:
            return super().get_queryset()
        queryset = Disorder.objects.all()
        symptom_name = queryset.filter(name=name)
        queryset = symptom_name
        return queryset


class FilterSymptoms(ListAPIView):
    queryset = Symptom.objects.all()


class SymptomsList(ListAPIView):
    """ View Symptoms
        able to filter by name
    """
    queryset = Symptom.objects.all()
    serializer_class = SymptomsSerializer
    filter_backends = (DjangoFilterBackend,)
    fields = ('name')
    pagination_class = ViewPagination

    def get_queryset(self):
        name = self.request.query_params.get('name', None)
        if name is None:
            return super().get_queryset()
        queryset = Symptom.objects.all()
        symptom_name = queryset.filter(name=name)
        queryset = symptom_name
        return queryset
