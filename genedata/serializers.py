from rest_framework import serializers
from .models import *

#serializer for our gene model
#Serializers allow complex data such as querysets and model instances to be converted to
#native Python datatypes that can then be easily rendered into JSON, XML or other content types. 
#Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data.


class ECSerializer(serializers.ModelSerializer):
    class Meta:
        model = EC
        fields = ['id', 'ec_name']

class SequencingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sequencing
        fields = ['id', 'sequencing_factory', 'factory_location']


class GeneSerializer(serializers.ModelSerializer):
    ec = ECSerializer()
    sequencing = SequencingSerializer()
    class Meta:
        model = Gene
        fields = ['gene_id', 'entity', 'start', 'stop', 'sense', 'start_codon', 'ec', 'sequencing']
    # data that user will provide for ec and sequencing is not stored in a gene table 
    # rewrite default save() to make input handled appropriately
    def create(self, validated_data):
        ec_data = self.initial_data.get('ec')
        seq_data = self.initial_data.get('sequencing')
        #we want to correctly link these foreign key fields in the gene table to the records in the correct EC or sequencing table
        # so we look up at row in the EC table based on the data that I got from the user.
        gene = Gene(**{**validated_data,
                    'ec' : EC.objects.get(pk=ec_data['id']),
                    'sequencing': Sequencing.objects.get(pk=seq_data['id']) 
                    })
        gene.save()
        return gene


class GeneListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gene
        fields = ['id', 'gene_id']