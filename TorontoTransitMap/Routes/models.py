from django.db import models
from Stops.models import Trip
from Vehicle.models import Vehicle  # Adjust the import based on your actual app structure
# Create your models here.

# route_id,agency_id,route_short_name,route_long_name,route_desc,route_type,route_url,route_color,route_text_color
class Route(models.Model):
    route_key = models.IntegerField(blank=False, null=False)
    name = models.CharField(blank=False, null=False, max_length=255)
    trips = models.ManyToManyField(Trip, blank=False)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, blank=False, null=True)

    def __str__(self):
        return self.name