from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Product
from products.serializers import ProductSerializer
from .pagination import CustomPagination

@api_view(["GET", "POST"])
def index(request):
    """
    DRF API View
    """
    if request.method == 'GET':
        # instance = Product.objects.all().order_by("?").first()
        # data = {}
        # if instance:
        #     serializer = ProductSerializer(
        #         instance, context={'request': request})
        #     data = serializer.data
        # return Response(data)
        qs = Product.objects.all()
        paginator = CustomPagination()

        result = paginator.paginate_queryset(qs, request)
        if result is not None:
            serializer = ProductSerializer(result, context = {'request': request}, many = True)
            return paginator.get_paginated_response(serializer.data)
        
        serializer = ProductSerializer(qs, context = {'request': request}, many = True)
        return Response(serializer.data)
        

    if request.method == 'POST':
        serializer = ProductSerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
