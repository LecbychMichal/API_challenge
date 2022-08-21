from rest_framework import serializers
from .models import Countries


class CountryListSerializer(serializers.ModelSerializer):


    class Meta:
        model = Countries
        fields = ['name', 'countryCode', 'id', 'createdAt']


