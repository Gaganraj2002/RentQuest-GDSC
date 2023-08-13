from django.urls import path
from .views import apartmentView
from .api_views import (
    ApartmentList,
    ApartmentDetail,
    InquiryList,
    InquiryDetail,
    ApartmentSearchAPIView,
    ApartmentCreateAPIView,
    SavedApartmentListCreateAPIView,
    SavedApartmentDetailAPIView,
)


urlpatterns = [
    path("apartments/", ApartmentList.as_view(), name="apartment-list"),
    path("apartments/<int:pk>/", ApartmentDetail.as_view(), name="apartment-detail"),
    path("inquiries/", InquiryList.as_view(), name="inquiry-list"),
    path("inquiries/<int:pk>/", InquiryDetail.as_view(), name="inquiry-detail"),
    path("search/", ApartmentSearchAPIView.as_view(), name="apartment-search"),
    path("<int:id>/", apartmentView, name="apartView"),
    path(
        "api/apartments/create/",
        ApartmentCreateAPIView.as_view(),
        name="create-apartment",
    ),
    path(
        "api/saved-apartments/",
        SavedApartmentListCreateAPIView.as_view(),
        name="saved-apartment-list",
    ),
    path(
        "api/saved-apartments/<int:pk>/",
        SavedApartmentDetailAPIView.as_view(),
        name="saved-apartment-detail",
    ),
]
