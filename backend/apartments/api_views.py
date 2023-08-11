from rest_framework import generics
from rest_framework.filters import SearchFilter
from .models import Apartment
from .serializers import ApartmentSerializer


class ApartmentSearchAPIView(generics.ListAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    filter_backends = [SearchFilter]
    search_fields = [
        "title",
        "description",
        "location",
        "price",
    ]  # Add other fields as needed
