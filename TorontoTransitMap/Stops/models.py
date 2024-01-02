from django.db import models

class Trip(models.Model):
    trip_id = models.IntegerField(unique=True, blank=False, null=False)
    route_id = models.ForeignKey("Routes.Route", on_delete=models.CASCADE)
    arrival_time = models.TimeField()
    departure_time = models.TimeField()

    def __str__(self):
        return f"Trip {self.trip_id}"

class Stop(models.Model):
    stop_id = models.IntegerField(blank=False, unique=True)
    stop_code = models.IntegerField(blank=False, null=False, unique=True)
    stop_name = models.CharField(blank=False, null=False, max_length=255)
    stop_lat = models.DecimalField(blank=False, null=False, max_digits=9, decimal_places=6)
    stop_lon = models.DecimalField(blank=False, null=False, max_digits=9, decimal_places=6)
    wheelchair_boarding = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return f"Stop {self.stop_id}: {self.stop_name}"

class StopTime(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    stop = models.ForeignKey(Stop, on_delete=models.CASCADE)
    stop_sequence = models.IntegerField()

    def __str__(self):
        return f"{self.trip} - Stop {self.stop_sequence}: {self.stop}"
