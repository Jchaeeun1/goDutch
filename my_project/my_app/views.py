from django.shortcuts import render
from django.http import JsonResponse
from .models import Item

def index(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request, 'index.html', context)

def get_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    data = {
        'name': item.name,
        'price': item.price,
        'description': item.description
    }
    return JsonResponse(data)
