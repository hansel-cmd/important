from rest_framework import serializers
from rest_framework.reverse import reverse
from rest_framework.validators import UniqueValidator

from .models import Product
from .validators import validate_price

from api.serializers import UserPublicDataSerializer


class ProductSerializer(serializers.ModelSerializer):

    # owner = UserPublicDataSerializer(source = 'user', read_only = True) # This or the below
    user = UserPublicDataSerializer(read_only = True)
    custom_attribute = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()
    edit_url = serializers.HyperlinkedIdentityField(view_name = 'product-edit', lookup_field = 'pk')

    price = serializers.DecimalField(validators = [validate_price], max_digits=15, decimal_places=2)
    # title = serializers.CharField(validators = [UniqueValidator(queryset=Product.objects.all(), lookup = 'iexact')])

    class Meta:
        model = Product
        fields = [
            'user',
            'id',
            'title',
            'content',
            'price',
            'sale_price',
            'custom_attribute',
            'url',
            'edit_url',
            'public'
        ]
    
    def validate_title(self, value):
        """
        You can check for uniqueness via:
        from rest_framework.validators import UniqueValidator
        title = serializers.CharField(validators = [UniqueValidator(queryset=Product.objects.all(), lookup = 'iexact')])

        By uniqueness, we mean:
            - The title is unique regardless of whether who the creator is (admin or staff)
        
        """
        request = self.context.get('request')
        user = request.user if request else None
        qs = Product.objects.filter(title__iexact = value)
        if qs.exists():
            raise serializers.ValidationError(f"{value} is already a title! :(")
        return value

    def get_url(self, instance):
        # sometimes, self.request is not present, you must get it using context
        request = self.context.get('request')
        if request is None:
            return None
        print(instance)
        return reverse("product-detail", kwargs={'pk': instance.pk}, request = request)

    def get_custom_attribute(self, instance):
        return instance.__str__()
        