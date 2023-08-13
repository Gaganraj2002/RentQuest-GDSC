from django.db import models
from django.contrib.auth.models import User


class Apartment(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.PositiveIntegerField()
    landlord = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class ApartmentImage(models.Model):
    apartment = models.ForeignKey(
        Apartment, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="apartment_images/%Y/%m/%d/")

    def __str__(self):
        return f"Image of {self.apartment.title}"


class Inquiry(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Inquiry about {self.apartment.title} by {self.name}"


class SavedApartment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} saved {self.apartment.title}"
