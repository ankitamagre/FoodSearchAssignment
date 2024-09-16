from rest_framework import serializers
from . models import ToppingsGroupModel, ToppingsModel, ProductModel, RatingModel, ProductToppingModel


class ToppingsGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToppingsGroupModel
        fields = ['group_name']



class ToppingSerializer(serializers.ModelSerializer):
    group = ToppingsGroupSerializer()

    class Meta:
        model = ToppingsModel
        fields = ['topping_name', 'group']


class ProductSerializer(serializers.ModelSerializer):
     class Meta:
        model = ProductModel
        fields = ['product_name', 'product_description', 'product_category', 'veg_non_veg']



class RatingSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = RatingModel
        fields = ['product_name', 'rating_value']


class ProductToppingSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    topping = ToppingSerializer
    class Meta:
        model = ProductToppingModel
        fields = ['product', 'topping']