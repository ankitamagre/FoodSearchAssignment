import django_filters 
from . models import ProductModel
from django.db.models import Q
from django.core.exceptions import ValidationError

class ProductFilter(django_filters.FilterSet):
    

    min_rating = django_filters.NumberFilter(field_name='ratingmodel__rating_value', lookup_expr='gte')
    max_rating = django_filters.NumberFilter(field_name='ratingmodel__rating_value', lookup_expr='lte')


    product_category = django_filters.CharFilter(method='filterByProduct')


    veg_non_veg = django_filters.ChoiceFilter(choices = ProductModel.product_type_choices)


    toppings = django_filters.CharFilter(method='filterByToppings')


    class Meta:
        model = ProductModel
        fields = ['min_rating', 'max_rating', 'product_category', 'veg_non_veg', 'toppings']

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)
        return queryset.distinct()


    def filterByProduct(self, queryset, name, value):
        category_names = value.split(',') 

        

        q_obj = Q()
        for name in category_names:   
            q_obj |= Q(product_category__iexact = name.strip())
            
        return queryset.filter(q_obj)    
    

    def filterByToppings(self, queryset, name, value):
        topping_names = value.split(',')

        q_obj = Q()
        for topping in topping_names:
            q_obj |= Q(producttoppingmodel__topping__topping_name__iexact = topping.strip())

        return queryset.filter(q_obj).distinct()
        

    # def validate_data(self, data):
    #     min_rating = data.get('min_rating')
    #     max_rating = data.get('max_rating')

    #     if min_rating > max_rating:
    #         raise ValidationError('min rating cannot be greater than max rating')