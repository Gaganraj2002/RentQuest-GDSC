from django.urls import path
from .views import apartmentView
from .api_views import (
    ApartmentList,
    ApartmentDetail,
    InquiryList,
    InquiryDetail,
    ApartmentSearchAPIView,
)


urlpatterns = [
    path("apartments/", ApartmentList.as_view(), name="apartment-list"),
    path("apartments/<int:pk>/", ApartmentDetail.as_view(), name="apartment-detail"),
    path("inquiries/", InquiryList.as_view(), name="inquiry-list"),
    path("inquiries/<int:pk>/", InquiryDetail.as_view(), name="inquiry-detail"),
    path("search/", ApartmentSearchAPIView.as_view(), name="apartment-search"),
    path("<int:id>/", apartmentView, name="apartView"),
]
