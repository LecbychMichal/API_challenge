from .models import Countries
from .serializers import CountryListSerializer, CountryDetailSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from .paginations import CustomPagination


class CountryListView(ListCreateAPIView):
    queryset = Countries.objects.all()
    serializer_class = CountryListSerializer
    pagination_class = CustomPagination

class CountryDetailView(RetrieveUpdateAPIView):
    queryset = Countries.objects.all()
    serializer_class = CountryDetailSerializer