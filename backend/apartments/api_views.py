from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from .serializers import (
    ApartmentSerializer,
    InquirySerializer,
    SavedApartmentSerializer,
)
from .models import Apartment, Inquiry, SavedApartment


class ApartmentCreateAPIView(generics.CreateAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer


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


class SavedApartmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = SavedApartment.objects.all()
    serializer_class = SavedApartmentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SavedApartmentDetailAPIView(generics.RetrieveDestroyAPIView):
    queryset = SavedApartment.objects.all()
    serializer_class = SavedApartmentSerializer
    permission_classes = [IsAuthenticated]
