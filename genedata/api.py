from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *

@csrf_exempt
def gene_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        gene = Gene.objects.get(pk=pk)
    except Gene.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = GeneSerializer(gene)
        return JsonResponse(serializer.data)


@csrf_exempt
def genes_list(request):
    if request.method == 'GET':
        gene = Gene.objects.all()
        serializer = GeneListSerializer(gene, many=True)
        return JsonResponse(serializer.data, safe=False)




