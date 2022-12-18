from rest_framework import serializers
from .models import *

#serializer for our gene model
#class GeneSerializer(serializers.Serializer):
    # gene_id = serializers.CharField(required=True, allow_blank=False, max_length=256)
    # entity = serializers.CharField(required=True, allow_blank=False, max_length=256)
    # start = serializers.IntegerField()

class GeneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gene
        fields = ['gene_id', 'entity', 'start', 'stop', 'sense', 'start_codon']



class GeneListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gene
        fields = ['id', 'gene_id']