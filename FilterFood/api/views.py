from . models import ProductModel
from. serializers import ProductSerializer
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend 
from . filters import ProductFilter
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page'
    max_page_size = 10

class ProductView(ListAPIView):
    pagination_class = CustomPagination

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

