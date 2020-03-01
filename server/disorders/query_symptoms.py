from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response


class QueryList(APIView):

    parser_classes = [JSONParser]

    @csrf_exempt
    def post(self, request, format=None):
        return Response(request.data)
