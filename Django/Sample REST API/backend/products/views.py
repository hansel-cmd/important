from rest_framework import generics
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework import permissions

from api.authentication import TokenAuthentication
from .models import Product
from .serializers import ProductSerializer
from .permissions import TestPermission
from .mixins import UserQuerySetMixin


class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    # Override destroy to return a custom response.
    # By default, destroy() function does not return anything.
    # It only returns a status 204 No Content.
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        data = ProductSerializer(
            instance, context={'request': request}).data
        print("kwargs", kwargs)
        instance.delete()
        return Response(data, status=200)


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


class ProductListCreateAPIView(UserQuerySetMixin, generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [
        authentication.SessionAuthentication,  # Good for django/in-house application
        # authentication.TokenAuthentication # Override keyword so we use TokenAuthentication which we created
        TokenAuthentication
    ]
    permission_classes = [
        # permissions.IsAdminUser,
        permissions.IsAuthenticated,
        # TestPermission,
    ]
    # lookup_field = 'pk'

    # If you want to have extra functionality before you save,
    # then modify this function. The def save() will validate it for us before
    # calling this function.
    def perform_create(self, serializer):
        print(serializer.validated_data)
        content = serializer.validated_data.get('content')
        if not content:
            content = serializer.validated_data.get('title')
        serializer.save(user=self.request.user, content=content)


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'
    permission_classes = []  # To override default settings

    def perform_create(self, serializer):
        print(serializer.validated_data)
        content = serializer.validated_data.get('content')
        if not content:
            content = serializer.validated_data.get('title')
        serializer.save(user = self.request.user, content=content)


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'
