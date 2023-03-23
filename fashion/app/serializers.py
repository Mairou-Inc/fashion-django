from app.models import *
from rest_framework import serializers



class SizeSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField('get_title')
    price = serializers.SerializerMethodField('get_price')


    def get_title(self, obj):
        return obj.name
    
    def get_price(self, obj):
        print(Price.objects.get(size_id=obj))
        return 22

    class Meta:
        model = Size
        fields = ['title', 'price']



class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name']

class ProductSerializer(serializers.ModelSerializer):
    # brand = BrandSerializer(many=False)
    size = SizeSerializer(many=True)
    brand_name = serializers.SerializerMethodField('get_brand_name')
    actual_price = serializers.SerializerMethodField('get_actual_price')

    def get_brand_name(self, obj):
        return obj.brand.name
    
    def get_actual_price(self, obj):
        return Price.objects.filter(size__product=obj).order_by('-updatedAt').first().price

    class Meta:
        model = Product
        fields = [ 'name', 'sku', 'brand_name','actual_price', 'size']



# {
#    "title": "Ботинки",
#    "sku": "АБВ1",
#    "price": 70000,
#    "brand_name": "GUCCI",
#    "size": [
#        {
#            "title": "42",
#            "price": 70000
#        },
#        {
#            "title": "43",
#            "price": 75000
#        }
#    ]
# }
