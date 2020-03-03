from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from .models import Symptom
from .serializers import SymptomsSerializer

from nltk.corpus import stopwords
from functools import reduce
import operator


import nltk
nltk.download('punkt')
nltk.download('stopwords')


class ProcessRequest(object):
    def __init__(self, text,  symptoms=[]):
        self.text = text
        self.symptoms = self.tokenize()

    def tokenize(self):
        """ remove the white spaces from text
        """
        stop_words = set(stopwords.words('english'))
        word_tokens = set(nltk.word_tokenize(self.text))
        filtered_sentence = word_tokens.difference(stop_words)
        # filtered_sentence = [w for w in word_tokens if w in stop_words]
        return filtered_sentence

    def get_symptoms(self):
        return self.symptoms


class QueryList(APIView):
    queryset = Symptom.objects.all()

    parser_classes = [JSONParser]
    serializer_class = SymptomsSerializer

    @csrf_exempt
    def post(self, request, format=None):
        processed_request = ProcessRequest(request.data['data'])
        queryset = Symptom.objects.all()
        symptoms = processed_request.get_symptoms()
        clauses = (Q(name__icontains=x) for x in symptoms)
        query = reduce(operator.or_, clauses)
        queryset = queryset.filter(query)
        disorders = list(queryset.values('disorders__name')
                         .annotate(count=Count('disorders__name'))
                         .order_by("-count"))
        return JsonResponse(disorders, safe=False)
        # TODO: Stemming filter: need to create
        # stemming function in ProcessRequest and get  new
        # symptoms (EX: obesity -> obes which yields invalid results)
        # Find/create medical stemming
