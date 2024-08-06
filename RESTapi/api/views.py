from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerializer

@api_view(['GET'])
def getData(request):
    Items = Item.objects.all()
    serializer = ItemSerializer(Items, many=True) # many is given for serializing multiple data instances
    
    return Response(serializer.data) # SHOWS DRF UI

@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def updateItem(request, pk):
    item = Item.objects.get(id=pk)

    serializer = ItemSerializer(item, data= request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteItem(request, pk):
    item = Item.objects.get(id=pk)

    item.delete()
    return Response()

