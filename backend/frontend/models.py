from django.db import models


class SiteConfiguration(models.Model):
    site_name = models.CharField(max_length=100)
    welcome_message = models.TextField()

    def __str__(self):
        return self.site_name


# Other models related to frontend configuration or content can be added here
