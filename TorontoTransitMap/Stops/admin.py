from django.contrib import admin
from .models import Stop, StopTime, Trip

# Register your models here.
admin.site.register(Stop)
admin.site.register(StopTime)
admin.site.register(Trip)