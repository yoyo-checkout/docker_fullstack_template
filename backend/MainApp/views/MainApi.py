from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
# from rest_framework.parsers import JSONParser
# import requests

from MainApp.models import TemplateModel
from MainApp.serializers import TemplateSerializer

# Create your views here.
@csrf_exempt
def MainApi(_request):
    data = TemplateModel.objects.all()
    response = TemplateSerializer(data, many = True)
    return JsonResponse(response.data, safe = False)
