from rest_framework import routers
from .views import InquiryViewSet
from .views import create_inquiry
from django.urls import path

router = routers.DefaultRouter()
router.register(r"inquiries", InquiryViewSet)

urlpatterns = router.urls

urlpatterns = [
    # ...
    path("create/", create_inquiry, name="inquiry-create"),
    # ...
]
