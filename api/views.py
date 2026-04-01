from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

# GET all products
@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

# POST new product
@api_view(['POST'])
def create_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

# GET single product
@api_view(['GET'])
def get_product(request, id):
    product = Product.objects.get(id=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

# PUT update product
@api_view(['PUT'])
def update_product(request, id):
    product = Product.objects.get(id=id)
    serializer = ProductSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

# DELETE product
@api_view(['DELETE'])
def delete_product(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return Response({"message": "Deleted successfully"})