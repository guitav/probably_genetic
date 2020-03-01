from django.http import HttpResponse
from django.core import serializers
from .serializers import SymptomsSerializer, DisordersSerializer
from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .models import Symptoms, Disorder
import nltk
nltk.download('punkt')


class ProcessRequest(object):
    def __init__(self, text,  symptoms=[]):
        self.text = text
        self.symptoms = self.tokenize()

    def tokenize(self):
        """ remove the white spaces from text
        """
        return nltk.word_tokenize(self.text)

    def get_symptoms(self):
        return self.symptoms


class QueryList(APIView):
    queryset = Symptoms.objects.all()

    parser_classes = [JSONParser]
    serializer_class = SymptomsSerializer

    @csrf_exempt
    def post(self, request, format=None):
        processed_request = ProcessRequest(request.data['data'])
        queryset = Symptoms.objects.all()
        queryset = queryset.filter(name__in=processed_request.get_symptoms())
        disorders = list(queryset.values('disorders__name').annotate(count=Count('disorders__name')).order_by("-count"))
        return JsonResponse(disorders, safe=False)
        # return Response(request.data)


# set up to be able to query by multiple disorders,
# filter by the overlapping
# intersection of multiple lists
# if one does not fit remove best one?
# if there  is no intersection then skip that one and keep going
# algorithm for highest intersection  of attributes
# vectorize for familiar / common illnesses / when you are adding in new ones
# account  for  if they look up testing ;; that should be trigger word
# need to  add function comments for everything
#
