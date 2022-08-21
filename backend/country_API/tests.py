from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Countries
from .paginations import CustomPagination


class CountryListView(APITestCase):

    def test_create_country_created_and_country_count(self):
        """
        Testing for the response status and if only 1 object was added to the database 
        """
        count = Countries.objects.all().count()
        object = {"name": "Czech Republic", "countryCode": "CZ"}

        response = self.client.post(reverse('countries'), object)
        country = Countries.objects.get()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        new_count = Countries.objects.all().count()
        self.assertEqual(new_count, count+1)