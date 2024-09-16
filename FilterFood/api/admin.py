# from django.contrib import admin
# from . models import CategoryModel, CustomizationModel, ToppingsModel, ProductModel

# @admin.register(CategoryModel)
# class  CategoryAdmin(admin.ModelAdmin):
#     list_display = ['cat_name']


# @admin.register(CustomizationModel)
# class  CustomizationAdmin(admin.ModelAdmin):
#     list_display = ['customize_name', 'get_toppings']

#     def get_toppings(self, obj):
#         return ", ".join([topping.topping_name for topping in obj.topping.all()])
    
#     get_toppings.short_description = 'Toppings'  


# @admin.register(ToppingsModel)
# class  ToppingsAdmin(admin.ModelAdmin):
#     list_display = ['topping_name']


# @admin.register(ProductModel)
# class  ProductAdmin(admin.ModelAdmin):
#     list_display = ['prd_name', 'desc', 'price', 'rating', 'category', 'get_customizations', 'prd_type']

#     def get_customizations(self, obj):
#         return ", ".join([customize.customize_name for customize in obj.customize.all()])

#     get_customizations.short_description = 'Customizations'
    