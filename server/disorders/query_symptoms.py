from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from functools import reduce
from django.db.models import Q
# from nltk.tokenize import RegexpTokenizer
import operator
from .models import Symptom
from .serializers import SymptomsSerializer

from nltk.corpus import stopwords
import nltk
from nltk.tokenize import MWETokenizer
import regex as re
nltk.download('punkt')
nltk.download('stopwords')


class ProcessRequest(object):
    """ Process the text received from form  post
    """

    def __init__(self, text,  symptoms=[]):
        self.text = text
        self.symptoms = []
        self.find_common_symptoms()
        self.parse()
        SYMPTOM_REGEX = ['(\btype)*(\w)+|(\w*somy [^\s]+)|([^\s]+ syndrome\b)']

    def find_common_symptoms(self):
        SYMPTOM_REGEX = '\btype*\w+|\w*somy [^\s]+|[^\s]+ syndrome\b'
        regex = r'\btype [^\s]+|\w*somy [^\s]+|[^\s]+ syndrome\b'
        self.symptoms += re.findall(regex, self.text)
        self.text = re.sub(regex, '', self.text)

    def parse(self):
        """ tokenize and remove stop words
        """

        stop_words = set(stopwords.words('english'))
        word_tokens = set(nltk.word_tokenize(self.text))
        print (self.text)
        filtered_sentence = word_tokens.difference(stop_words)
        # new_sent = list(filtered_sentence)
        # print(tokenizer.tokenize(new_sent))
        print (self.symptoms)
        # phrases = Phrases(filtered_sentence, min_count=1, threshold=1)
        # print(phrases)
        return filtered_sentence

    def get_symptoms(self):
        return self.symptoms


class Search(APIView):

    queryset = Symptom.objects.all()
    parser_classes = [JSONParser]
    serializer_class = SymptomsSerializer

    @csrf_exempt
    def post(self, request, format=None):
        """ get post request and query disorders from symptoms
        """
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
