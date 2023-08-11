from django.db import models
from apartments.models import Apartment
from django.contrib.auth.models import User


class Inquiry(models.Model):
    apartment = models.ForeignKey(
        Apartment, on_delete=models.CASCADE, related_name="inquiries"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inquiry about {self.apartment} by {self.user}"
