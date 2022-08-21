from .models import Countries
from .serializers import CountryListSerializer
from rest_framework.generics import ListCreateAPIView


class CountryListView(ListCreateAPIView):
    queryset = Countries.objects.all()
    serializer_class = CountryListSerializer

