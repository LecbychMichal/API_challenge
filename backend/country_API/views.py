from .models import Countries
from .serializers import CountryListSerializer, CountryDetailSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from .paginations import CustomPagination


class CountryListView(ListCreateAPIView):
    """
    Post and get method for listing all the countries.
    """
    queryset = Countries.objects.all()
    serializer_class = CountryListSerializer
    pagination_class = CustomPagination

class CountryDetailView(RetrieveUpdateAPIView):
    """
    Put/Patch and get method for each country.
    """
    queryset = Countries.objects.all()
    serializer_class = CountryDetailSerializer