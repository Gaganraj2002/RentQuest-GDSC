from rest_framework import generics
from .models import Apartment, Inquiry
from .serializers import ApartmentSerializer, InquirySerializer

from django.shortcuts import render, redirect


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


def apartmentView(request, id):
    apartment = Apartment.objects.get(id=id)
    inquiry = Inquiry.objects.filter(apartment=apartment)
    data = {"apartment": apartment, "inquiries": inquiry}
    return render(request, "apartments/apartment_detail.html", data)
