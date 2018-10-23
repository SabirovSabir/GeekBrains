from django.shortcuts import render
import json

def products_list(request):
    context = {}

    with open('products/data/products.json', 'r') as file:
        context = json.load(file)

    return render(request, 'products/list.html', context)

#TODO Get only one product
def products_detail(request, idx):
    context = {}

    with open('products/data/products.json', 'r') as file:
        context = json.load(file)

    return render(
        request,
        'products/detail.html', {
        'object': context['products'][idx]
    } )