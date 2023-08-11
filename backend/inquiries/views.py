from rest_framework import viewsets
from .models import Inquiry
from .serializers import InquirySerializer
from django.shortcuts import render
from apartments.models import Apartment


class InquiryViewSet(viewsets.ModelViewSet):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer


def create_inquiry(request):
    if request.method == "POST":
        apartment_id = request.POST.get("apartment")
        message = request.POST.get("message")
        # Create the inquiry in the database
        Inquiry.objects.create(
            apartment_id=apartment_id, user=request.user, message=message
        )
        return render(request, "inquiries/inquiry_success.html")
    else:
        apartments = Apartment.objects.all()
        return render(
            request, "inquiries/inquiry_form.html", {"apartments": apartments}
        )
