from rest_framework import serializers
from .models import Apartment, Inquiry, ApartmentImage, SavedApartment


class InquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = "__all__"


class ApartmentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentImage
        fields = ("image",)


class ApartmentSerializer(serializers.ModelSerializer):
    images = ApartmentImageSerializer(
        many=True, required=False
    )  # Handle multiple images

    class Meta:
        model = Apartment
        fields = [
            "id",
            "title",
            "description",
            "location",
            "price",
            "bedrooms",
            "landlord",
            "images",
        ]

    def create(self, validated_data):
        images_data = self.context.get("view").request.FILES  # Get uploaded images
        apartment = Apartment.objects.create(**validated_data)

        for image_data in images_data.values():
            ApartmentImage.objects.create(apartment=apartment, image=image_data)

        return apartment


class SavedApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedApartment
        fields = "__all__"
