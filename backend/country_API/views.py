from .models import Countries
from .serializers import CountryListSerializer, CountryDetailSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from .paginations import CustomPagination
from django_filters.rest_framework import DjangoFilterBackend


class CountryListView(ListCreateAPIView):
    """
    Post and get method for listing all the countries. Query by countryCode
    """
    queryset = Countries.objects.all()
    serializer_class = CountryListSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['countryCode']

class CountryDetailView(RetrieveUpdateAPIView):
    """
    Put/Patch and get method for each country.
    """
    queryset = Countries.objects.all()
    serializer_class = CountryDetailSerializer