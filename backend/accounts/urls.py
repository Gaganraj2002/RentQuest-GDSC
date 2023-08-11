from django.urls import path
from .api_views import RegisterAPIView, LoginAPIView, LogoutAPIView
from .views import landlord_registration

urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="register"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("logout/", LogoutAPIView.as_view(), name="logout"),
    path("registration/", landlord_registration, name="landlord-registration"),
]
