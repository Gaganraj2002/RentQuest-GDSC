from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *


class UserView(APIView):
    def get(self, request):
        output = [
            {
                "site_name": output.site_name,
                "welcome_message": output.welcome_message,
            }
            for output in SiteConfiguration.objects.all()
        ]
        return Response(output)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


class helloWorld(APIView):
    def get(self, request):
        return Response({"message": "Hello World!"})

    def post(self, request):
        return Response({"message": "Hello World!"})
