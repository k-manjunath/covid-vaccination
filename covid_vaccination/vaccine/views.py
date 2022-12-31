from django.shortcuts import render, redirect

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView


from .models import VaccinationCenter, Booking
from .forms import BookVaccineForm

# Create your views here.
def home(request):
    centers = VaccinationCenter.objects.all()
    context = {
        'title': 'Home',
        'centers': centers
    }
    return render(request, 'vaccine/home.html', context)

def search_center(request):
    context = {
        'title': 'Search',

    }
    return render(request, 'vaccine/search_center.html', context)
#check booking form
class BookVaccineView(LoginRequiredMixin, CreateView):
    model = Booking
    fields = ['time', 'center']
    def form_valid(self, form):
        form.instance.center_id = form.fields[self.kwargs['center']]
        return super().form_valid(form)