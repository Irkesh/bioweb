import factory
from django.test import TestCase
from django.conf import settings
from django.core.files import File

#as our fixtures represent all our models in a databse we have to represent our models
from .models import *

class ECFactory(factory.django.DjangoModelFactory):
    ec_name = "transferase"

    class Meta:
        model = EC

class SequencingFactory(factory.django.DjangoModelFactory):
    sequencing_factory = "Sanger"
    factory_location = "UK"

    class Meta:
        model = Sequencing


class GeneFactory(factory.django.DjangoModelFactory):
    gene_id = "GeneX"
    entity = "Plasmid"
    start = 12
    stop = 100
    sense = "+"
    start_codon = "M"
    sequencing = factory.SubFactory(SequencingFactory)
    ec = factory.SubFactory(ECFactory)
    access = 0

    class Meta:
        model = Gene
