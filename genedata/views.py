from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from .forms import *


def index(request):
    master_genes = Gene.objects.all()
    return render(request, 'genedata/index.html', {'master_genes': master_genes})


def gene(request, pk):
    gene = Gene.objects.get(pk=pk)
    gene.access += 1
    print("Gene record:", pk, "access count:", str(gene.access))
    gene.save()
    master_genes = Gene.objects.all()
    return render(request, 'genedata/gene.html', {'gene': gene, 'master_genes': master_genes})


def list(request, type):
    genes = Gene.objects.filter(entity__exact=type)
    master_genes = Gene.objects.all()
    return render(request, 'genedata/list.html', {'genes': genes, 'type': type, 'master_genes': master_genes})


def poslist(request):
    genes = Gene.objects.filter(entity__exact='Chromosome').filter(sense__startswith='+')
    master_genes = Gene.objects.all()
    return render(request, 'genedata/list.html', {'genes': genes, 'type': 'PosList', 'master_genes': master_genes})


def delete(request, pk):
    GeneAttributeLink.objects.filter(gene_id=pk).delete()
    Gene.objects.filter(pk=pk).delete()
    return HttpResponseRedirect("/test")

def create_ec(request):
    master_genes = Gene.objects.all()
     # if POST - user has sent some data to us
    if request.method == 'POST':
        #data sent by user is available in this POST class variable
        #when we declare the form, we can pass the data into the form using this variable.
        form = ECForm(request.POST)
        #form objects provide us a way of validating data
        if form.is_valid():
            ec = EC()
            #populate columns of an ec table with provided(cleaned_data)
            ec.ec_name = form.cleaned_data['ec_name']
            ec.save()
        #show page again and form again
        return HttpResponseRedirect('/create_ec/')
    else:
        #show all the entries in EC table + shows blank form - instantiating one instance of Form class
        ecs = EC.objects.all()
        form = ECForm()
        return render(request, 'genedata/ec.html', {'form': form, 'ecs': ecs, 'master_genes': master_genes})



def create_gene(request):
    if request.method == 'POST':
        #creating form using model form
        form = GeneForm(request.POST)        
        if form.is_valid():
            gene = form.save()
            return HttpResponseRedirect('/create_gene/')
        
    else:
        master_genes = Gene.objects.all()
        form = GeneForm()
    return render(request, 'genedata/create_gene.html', {'form': form, 'master_genes': master_genes})