from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Seller, Buyer
from .serializers import SellerSerializer, BuyerSerializer

# Seller Views
@api_view(['GET', 'POST'])
def seller_list(request):
    if request.method == 'GET':
        sellers = Seller.objects.all()
        serializer = SellerSerializer(sellers, many=True)
        return Response({"Sellers": serializer.data})
    
    elif request.method == 'POST':
        serializer = SellerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def seller_detail(request, id):
    try:
        seller = Seller.objects.get(pk=id)
    except Seller.DoesNotExist:
        return Response({"error": "Seller not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SellerSerializer(seller)
        return Response({"Seller": serializer.data})
    
    elif request.method == 'PUT':
        serializer = SellerSerializer(seller, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Seller": serializer.data}, status=status.HTTP_200_OK)
        return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        seller.delete()
        return Response({"message": "Seller deleted"}, status=status.HTTP_204_NO_CONTENT)

# Buyer Views
@api_view(['GET', 'POST'])
def buyer_list(request):
    if request.method == 'GET':
        buyers = Buyer.objects.all()
        serializer = BuyerSerializer(buyers, many=True)
        return Response({"Buyers": serializer.data})
    
    elif request.method == 'POST':
        serializer = BuyerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def buyer_detail(request, id):
    try:
        buyer = Buyer.objects.get(pk=id)
    except Buyer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BuyerSerializer(buyer)
        return Response({"Buyer": serializer.data})
    
    elif request.method == 'PUT':
        serializer = BuyerSerializer(buyer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        buyer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
