from .models import Countries
from .serializers import CountryListSerializer, CountryDetailSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView


class CountryListView(ListCreateAPIView):
    queryset = Countries.objects.all()
    serializer_class = CountryListSerializer

class CountryDetailView(RetrieveUpdateAPIView):
    queryset = Countries.objects.all()
    serializer_class = CountryDetailSerializer