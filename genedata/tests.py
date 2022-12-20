import json
from django.test import TestCase
#reverse allows us to take a path in our urls.py file and turn it into actual url string
from django.urls import reverse
from django.urls import reverse_lazy

from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase

from .model_factories import *
from .serializers import *

#######################################################################
# Serializers tests
########################################################################
class GeneSerialiserTest(APITestCase):
    gene1 = None
    geneserializer = None

    def setUp(self):
        self.gene1 = GeneFactory.create(pk=1, gene_id="gene1")
        self.geneserializer = GeneSerializer(instance=self.gene1)

    def tearDown(self):
        EC.objects.all().delete()
        Sequencing.objects.all().delete()
        Gene.objects.all().delete()
        ECFactory.reset_sequence(0)
        SequencingFactory.reset_sequence(0)
        GeneFactory.reset_sequence(0)
        
    def test_geneSerilaiserHasCorrectFields(self):
        data = self.geneserializer.data
        self.assertEqual(set(data.keys()), set(['gene_id', 'sequencing', 'sense', 'start', 'stop', 'entity', 'ec', 'start_codon']))

    def test_geneSerilaiserGeneIDIsHasCorrectData(self):
        data = self.geneserializer.data
        self.assertEqual(data['gene_id'], "gene1")


#######################################################################
#API test
#######################################################################
# Create your tests here.
class GeneTest(APITestCase):

    gene1 = None
    gene2 = None
    good_url = ''
    bad_url = ''
    delete_url = ''

    def setUp(self):
        self.gene1 = GeneFactory.create(pk=1, gene_id="gene1")
        self.gene2 = GeneFactory.create(pk=2, gene_id="gene2")
        self.gene3 = GeneFactory.create(pk=3, gene_id="gene3")
        self.good_url = reverse('gene_api', kwargs={'pk': 1})
        self.bad_url = "/api/gene/H/"
        self.delete_url = reverse('gene_api', kwargs={'pk': 3})

    #clean up database before instantiating new instance of dummy database
    def tearDown(self):
        EC.objects.all().delete()
        Sequencing.objects.all().delete()
        Gene.objects.all().delete()
        ECFactory.reset_sequence(0)
        SequencingFactory.reset_sequence(0)
        GeneFactory.reset_sequence(0)



# every function that start with test_* wil be run automatically when we run our tests #
########################################################################################
    def test_geneDetailReturnsSuccess(self):       
        response = self.client.get(self.good_url, format='json')
        response.render()
        self.assertEqual(response.status_code, 200)
        #checkig  that the data thst has arrived is correct
        data = json.loads(response.content)
        #checking that contest has key word entity
        self.assertTrue('entity' in data)
        #checing that value under ket entiry is Plasmid
        self.assertEqual(data['entity'], 'Plasmid')


#what if user sends something malformated:
    def test_geneDetailReturnFailOnBadPk(self):
        response = self.client.get(self.bad_url,format='json')
        #checking that malformated data causes 404 response (as it should)
        self.assertEqual(response.status_code, 404)

# test function for deleting gene
    def test_geneDetailDeleteIsSuccessful(self):
        response = self.client.delete(self.delete_url, format='json')
        self.assertEqual(response.status_code, 204)
