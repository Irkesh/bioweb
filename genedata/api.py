from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins


from .models import *
from .serializers import *

@api_view(['GET', 'POST'])
def gene_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
   
    """
    #Our serializer needs to handle Foreig keys from Gene model
    #sequencing = models.ForeignKey(Sequencing, on_delete=models.DO_NOTHING)
    #ec = models.ForeignKey(EC, on_delete=models.DO_NOTHING)
    if request.method == 'POST':
        serializer = GeneSerializer(data=request.data)
        #test wether the user data is corect respectivly to db model
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    try:
        gene = Gene.objects.get(pk=pk)
    except Gene.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = GeneSerializer(gene)
        return Response(serializer.data)





@api_view(['GET'])
def genes_list(request):
    try:
        gene = Gene.objects.all()
    except Gene.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':      
        gene = Gene.objects.all()  
        serializer = GeneListSerializer(gene, many=True)
        return Response(serializer.data)


# rewriting @api_view def genes_list(request): with one of the generics classes from rest_framework

class GeneList(generics.ListAPIView):
    queryset = Gene.objects.all()
    serializer_class = GeneListSerializer


class GeneDetails(mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):
    queryset = Gene.objects.all()
    serializer_class = GeneSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



