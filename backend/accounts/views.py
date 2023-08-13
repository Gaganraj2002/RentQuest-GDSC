from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LandlordRegistrationForm


def landlord_registration(request):
    if request.method == "POST":
        form = LandlordRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = LandlordRegistrationForm()
    return render(request, "registration/registration.html", {"form": form})
