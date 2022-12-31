from django.contrib import admin
from .models import VaccinationCenter, Booking

# Register your models here.
admin.site.register(VaccinationCenter)
admin.site.register(Booking)