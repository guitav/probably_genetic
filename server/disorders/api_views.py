from rest_framework.generics import ListAPIView
from .serializers import DisordersSerializer, SymptomSerializer
from .models import Disorder as DisordersModel
from .models import Symptom as SymptomsModel
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination
# TODO:  Create parent class for filter name queries? DRY


class ViewPagination(LimitOffsetPagination):
    """ 2 <= Pages < 5 for each view
    """
    default_limit = 1
    max_limit = 1


class Disorder(ListAPIView):
    """ View disorders
        able to filter by name
    """
    queryset = DisordersModel.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']
    pagination_class = ViewPagination
    serializer_class = DisordersSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name', None)
        if name is None:
            return super().get_queryset()
        queryset = DisordersModel.objects.all()
        disorder_name = queryset.filter(name=name)
        queryset = disorder_name
        return queryset


class FilterSymptoms(ListAPIView):
    queryset = SymptomsModel.objects.all()


class Symptom(ListAPIView):
    """ View Symptoms
        able to filter by name
    """
    serializer_class = SymptomSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']
    pagination_class = ViewPagination
    queryset = SymptomsModel.objects.all()

    def get_queryset(self):
        name = self.request.query_params.get('name', None)
        if name is None:
            return super().get_queryset()
        queryset = SymptomsModel.objects.all()
        symptom_name = queryset.filter(name=name)
        queryset = symptom_name
        return queryset
