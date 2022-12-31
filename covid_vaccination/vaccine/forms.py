from django import forms
from .models import VaccinationCenter, Booking

#widget
class DateTimePickerInput(forms.DateTimeInput):
        input_type = 'datetime'

class ExampleForm(forms.Form):
        my_date_time_field = forms.DateTimeField(widget=DateTimePickerInput)

class BookVaccineForm(forms.DateTimeField):
    
    widgets = {
        'my_date_time_field' : 'DateTimeInput()',
    }

    class Meta:
        model = Booking
        fields = ['my_date_time_field', 'center'] #- not working, stopped for now
        # fields = ['datetime', 'center']
        