from rest_framework.decorators import api_view
from rest_framework.response import Response

from base.models import Item
from .serializers import ItemSerializer
# Create your views here.

# homepage - GET

@api_view(['GET'])
def overview(request):
    endpoints = {
        'list items' : '/list/',
        '/item/<str:pk>/' : 'item-details',
        '/create/': 'create-item',
        '/item/<str:pk>/update/': 'update',
        '/item/<str:pk>/delete/' : 'delete'
    }

    return Response(endpoints)


# list items - GET
@api_view(['GET'])
def list_items(request):
    items = Item.objects.all()

    serializer = ItemSerializer(items, many=True)

    return Response(serializer.data)

# item details -GET
@api_view(['GET'])
def item_datails(request, pk):
    item = Item.objects.get(id=pk)

    serializer = ItemSerializer(item)
    return Response(serializer.data)


# create item - POST
@api_view(['POST'])
def create_item(request):
    serializer = ItemSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
# update item - PUT
@api_view(['PUT'])
def update_item(request, pk):
    item = Item.objects.get(id=pk)

    serializer = ItemSerializer(item, data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# delete item - DELETE
@api_view(['DELETE'])
def delete_item(request, pk):
    item = Item.objects.get(id=pk)

    item.delete()
    return Response()