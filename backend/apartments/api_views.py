from rest_framework import generics
from rest_framework.filters import SearchFilter
from .serializers import ApartmentSerializer, InquirySerializer
from .models import Apartment, Inquiry


class ApartmentSearchAPIView(generics.ListAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    filter_backends = [SearchFilter]
    search_fields = [
        "title",
        "description",
        "location",
        "price",
    ]


class ApartmentList(generics.ListCreateAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer


class ApartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer


class InquiryList(generics.ListCreateAPIView):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer


class InquiryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer
