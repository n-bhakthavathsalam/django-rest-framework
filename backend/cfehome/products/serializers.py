from rest_framework import serializers
from products.models import Product
from rest_framework.reverse import reverse
from . import validators
from api.serializers import UserPublicSerializer

class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user', read_only=True) 
    # my_user_data = serializers.SerializerMethodField(read_only=True)
    # my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field = 'pk')
    # email = serializers.EmailField(write_only=True)
    title  = serializers.CharField(validators=[validators.validate_title_no_hello, validators.unique_product_title])
    body = serializers.CharField(source='content')
    
    class Meta:
        model = Product

        fields = ['owner','url','edit_url','pk', 'title', 'body','price',
                  'sale_price'] #'email','my_user_data','my_discount',


    # def get_my_user_data(self, obj):
    #     return {
    #         "username": obj.user.username
    #     }

    # def validate_title(self, value):
    # validate the fields
    #     qs = Product.objects.filter(title__iexact = value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f'{value} is already a product name')
    #     return value

    # def create(self, validated_data):
    #     # return Product.objects.create(**validated_data)
    #     # email = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #     # print(email, obj)
    #     return obj
    
    # def update(self, instance, validated_data):
    #     email = validated_data.pop('email')
    #     return super().update(instance, validated_data)



    def get_url(self, obj):
        # return f"/api/prodcuts/{obj.pk}"
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-detail", kwargs={"pk": obj.pk}, request=request)
    
    def get_edit_url(self, obj):
        # return f"/api/prodcuts/{obj.pk}"
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)

    # def get_my_discount(self, obj):
    #     try:
    #         return obj.get_discount()
    #     except:
    #         return None

  