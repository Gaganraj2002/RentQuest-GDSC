from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LandlordRegistrationForm


class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_401_UNAUTHORIZED)


class LogoutAPIView(APIView):
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


def landlord_registration(request):
    if request.method == "POST":
        form = LandlordRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # Redirect to the login page
    else:
        form = LandlordRegistrationForm()
    return render(request, "registration/registration.html", {"form": form})
