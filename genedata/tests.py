import json
from django.test import TestCase
#reverse allows us to take a path in our urls.py file and turn it into actual url string
from django.urls import reverse
from django.urls import reverse_lazy

from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase

from .model_factories import *
from .serializers import *


# Create your tests here.
class GeneTest(APITestCase):
# every function that start with test_* wil be run automatically when we run our tests 
    def test_geneDetailReturnsSuccess(self):
        gene = GeneFactory.create(pk=1, gene_id="gene1")
        url = reverse('gene_api', kwargs={'pk': 1})
        response = self.client.get(url)
        response.render()
        self.assertEqual(response.status_code, 200)
#what if user sends something malformated:
    def test_geneDetailReturnFailOnBadPk(self):
        gene = GeneFactory.create(pk=2, gene_id="gene2")
        url = "/api/gene/H/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

