from django.db import models


class ToppingsGroupModel(models.Model):                              
    group_name = models.CharField(max_length=255)

    
    class Meta:
        db_table = 'toppings_goups'


class ToppingsModel(models.Model):
    topping_id = models.IntegerField(primary_key=True)
    topping_name = models.CharField(max_length=255)
    group = models.ForeignKey(ToppingsGroupModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'toppings'
    

class ProductModel(models.Model):

    veg = 'veg'
    non_veg = 'non-veg'
    product_type_choices = [(veg, 'veg'), (non_veg, 'non-veg')]

    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=255)
    product_description = models.TextField()
    product_category = models.CharField(max_length=255)
    veg_non_veg = models.CharField(max_length=10, choices=product_type_choices)
    
    class Meta:
        db_table = 'products'




class RatingModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    rating_value = models.DecimalField(max_digits=2, decimal_places=1)
    
    class Meta:
        db_table = 'ratings'


class ProductToppingModel(models.Model):
    topping = models.ForeignKey(ToppingsModel, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_toppings'