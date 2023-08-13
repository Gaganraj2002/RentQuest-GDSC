from .models import Apartment, Inquiry
from django.shortcuts import render, redirect


def apartmentView(request, id):
    apartment = Apartment.objects.get(id=id)
    inquiry = Inquiry.objects.filter(apartment=apartment)
    data = {"apartment": apartment, "inquiries": inquiry}
    return render(request, "apartments/apartment_detail.html", data)
