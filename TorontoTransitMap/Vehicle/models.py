from django.db import models

# Create your models here.

class AbstractVehicle(models.Model):
    company = models.ForeignKey("Company.Company", on_delete=models.CASCADE)
    model = models.CharField(blank=True, max_length=255)
    year = models.PositiveIntegerField(blank=True)

    class Meta:
        abstract = True  # Make this class abstract

class Vehicle(AbstractVehicle):
	class VehicleType(models.IntegerChoices):
		STREETCAR = 0, 'Streetcar'
		SUBWAY = 1, 'Subway'
		RT = 2, 'RT'
		BUS = 3, 'Bus'
		UNKNOWN = 4, 'Unknown'

	vehicle_type = models.IntegerField(choices=VehicleType, default=VehicleType.UNKNOWN)

	def __str__(self):
		return f"{self.company.name} {self.vehicle_type} - {self.model} ({self.year})"
